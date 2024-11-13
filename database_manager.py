import sqlite3
from application import JobApplication

class DatabaseManager:
    def __init__(self, db_name='applications.db'):
        self.db_name = db_name
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS job_applications (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           job_name TEXT,
                           company_name TEXT,
                           method TEXT,
                           referral TEXT,
                           date TEXT,
                           status TEXT
                           )
                           ''')
        conn.commit()
        conn.close()

    def add_application(self, application: JobApplication):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
                       INSERT INTO job_applications (job_name, company_name, method, referral, date, status)
                       VALUES (?, ?, ?, ?, ?, ?)
                       ''', (application.job_name, application.company_name, application.method, application.referral, application.date, application.status))
        conn.commit()
        conn.close()
        
    def get_all_applications(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM job_applications")
        rows = cursor.fetchall()
        conn.close()
        return rows