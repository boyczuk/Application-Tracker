import tkinter as tk
from tkinter import ttk
from application import JobApplication
from database_manager import DatabaseManager

db_manager = DatabaseManager()

selected_item_id = None 
edit_entry = None 

def save_data():
    job_title = job_title_entry.get()
    company_name = company_entry.get()
    method = method_entry.get()
    referral_yn = referral_entry.get()
    date = date_entry.get()
    status = status_entry.get()
    
    job_application = JobApplication(job_title, company_name, method, referral_yn, date, status)
    
    db_manager.add_application(job_application)
    
    print("Data Saved")

    job_title_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)
    method_entry.delete(0, tk.END)
    referral_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)

    populate_table()

def populate_table():
    for row in table.get_children():
        table.delete(row)

    rows = db_manager.get_all_applications()
    for row in rows:
        table.insert("", "end", iid=row[0], values=row[1:])

def on_double_click(event):
    global edit_entry, selected_item_id
    
    item = table.identify_row(event.y)
    column = table.identify_column(event.x)
    
    selected_item_id = item

    if item:
        x, y, width, height = table.bbox(item, column)
        current_value = table.item(item, "values")[int(column[1]) - 1]
        
        edit_entry = tk.Entry(table)
        edit_entry.insert(0, current_value)
        edit_entry.place(x=x, y=y, width=width, height=height)
        edit_entry.focus()
        
        edit_entry.bind("<Return>", lambda e: save_edit(item, column))

def save_edit(item, column):
    global edit_entry
    
    new_value = edit_entry.get()
    col_index = int(column[1]) - 1

    current_values = list(table.item(item, "values"))
    current_values[col_index] = new_value

    table.item(item, values=current_values)
    
    updated_application = JobApplication(
        job_name=current_values[0],
        company_name=current_values[1],
        method=current_values[2],
        referral=current_values[3],
        date=current_values[4],
        status=current_values[5]
    )
    db_manager.update_application(selected_item_id, updated_application)

    edit_entry.destroy()

root = tk.Tk()
root.title("Job Application Tracker")

form_frame = tk.Frame(root, padx=10, pady=10)
form_frame.pack(side="left", fill="y")

table_frame = tk.Frame(root, padx=10, pady=10)
table_frame.pack(side="right", fill="both", expand=True)

tk.Label(form_frame, text="Job Title:").pack(pady=(20,5))
job_title_entry = tk.Entry(form_frame)
job_title_entry.pack()

tk.Label(form_frame, text="Company:").pack(pady=5)
company_entry = tk.Entry(form_frame)
company_entry.pack()

tk.Label(form_frame, text="Method of application:").pack(pady=5)
method_entry = tk.Entry(form_frame)
method_entry.pack()

tk.Label(form_frame, text="Referral(Y/N):").pack(pady=5)
referral_entry = tk.Entry(form_frame)
referral_entry.pack()

tk.Label(form_frame, text="Date Applied:").pack(pady=5)
date_entry = tk.Entry(form_frame)
date_entry.pack()

tk.Label(form_frame, text="Application Status:").pack(pady=5)
status_entry = tk.Entry(form_frame)
status_entry.pack()

save_button = tk.Button(form_frame, text="Save", command=save_data)
save_button.pack(pady=(10,20))

table_scroll = ttk.Scrollbar(table_frame, orient="vertical")
table_scroll.pack(side="right", fill="y")

table = ttk.Treeview(
    table_frame,
    columns=("Job Title", "Company", "Method", "Referral", "Date", "Status"),
    show="headings",
    yscrollcommand=table_scroll.set
)

table.heading("Job Title", text="Job Title")
table.heading("Company", text="Company")
table.heading("Method", text="Method")
table.heading("Referral", text="Referral")
table.heading("Date", text="Date")
table.heading("Status", text="Status")

table.column("Job Title", anchor="center", width=150)
for col in ("Company", "Method", "Referral", "Date", "Status"):
    table.column(col, anchor="center", width=100)

table.pack(fill="both", expand=True)
table_scroll.config(command=table.yview)

table.bind("<Double-1>", on_double_click)

populate_table()

window_width, window_height = 1000, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.mainloop()
