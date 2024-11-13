import tkinter as tk
from application import JobApplication
from database_manager import DatabaseManager

db_manager = DatabaseManager()

def save_data():
    job_title = job_title_entry.get()
    company_name = company_entry.get()
    method = method_entry.get()
    referral_yn = referral_entry.get()
    date = date_entry.get()
    status = status_entry.get()
    
    job_application = JobApplication(job_title, company_name, method, referral_yn, date, status)
    try:
        db_manager.add_application(job_application)
    except Exception as e:
        print(f"An error has occured: {e}")
        
    print("Data Saved")
    
    job_title_entry.delete(0, tk.END)
    company_entry.delete(0, tk.END)
    method_entry.delete(0, tk.END)
    referral_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)
    
    
root = tk.Tk()
root.title("Job Application Tracker")

tk.Label(root, text="Job Title:").pack(pady=(20,5))
job_title_entry = tk.Entry(root)
job_title_entry.pack()

tk.Label(root, text="Company:").pack(pady=5)
company_entry = tk.Entry(root)
company_entry.pack()

tk.Label(root, text="Method of application:").pack(pady=5)
method_entry = tk.Entry(root)
method_entry.pack()

tk.Label(root, text="Referral(Y/N):").pack(pady=5)
referral_entry = tk.Entry(root)
referral_entry.pack()


tk.Label(root, text="Date Applied:").pack(pady=5)
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Application Status:").pack(pady=5)
status_entry = tk.Entry(root)
status_entry.pack()

save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack(pady=(10,20))

window_width, window_height = 300, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.mainloop()