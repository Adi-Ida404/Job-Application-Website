import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, DateTime
import os

db_connect_url=os.environ['DB_CONNECTION_URL']

engine = create_engine(    
  db_connect_url,
  connect_args=
  {
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    }
  })


  
  