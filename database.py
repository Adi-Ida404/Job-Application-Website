import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connect_url = os.environ['DB_CONNECTION_URL']

engine = create_engine(    
    db_connect_url,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

try:

    def load_job_from_db(id):
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
            rows = result.all()
            if len(rows) == 0:
                return None
            else:
                return rows[0]._asdict()
              
    def add_application_to_db(job_id, data):
        with engine.connect() as conn:
            query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
            conn.execute(query, {"job_id": job_id, "full_name": data['full_name'], "email": data['email'], "linkedin_url": data['linkedin_url'], "education": data['educations'], "work_experience": data['experience'], "resume_url": data['resume_url']})
              
except Exception as e:
    print(f"Error: {e}")

  


  
  