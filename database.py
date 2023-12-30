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
              
except Exception as e:
    print(f"Error: {e}")

  


  
  