class JobApplication:
    def __init__(self, job_name, company_name, method, referral, date, status):
        self.job_name = job_name
        self.company_name = company_name
        self.method = method
        self.referral = referral
        self.date = date
        self.status = status
    
    def __str__(self):
        return (f"JobApplication(job_name='{self.job_name}', company_name='{self.company_name}', "
                f"method='{self.method}', referral='{self.referral}', date='{self.date}', status='{self.status}')")