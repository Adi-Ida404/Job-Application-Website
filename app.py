from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Web Developer',
    'location': 'Remote', 
    'Salary':'Rs. 12,00,000',
    'skills':'HTML, CSS, JavaScript',
    'require':'1 yrs+ Experience in Relevant Field'
  },
  {
    'id':2,
    'title':'App Developer',
    'location':'San Francisco, USA', 
    'Salary':'$ 500,000 PA',
    'skills':'Python, Django, Flask',
    'require':'2 yrs+ Experience in Relevant Field'
  },
  {
    'id':3,
    'title':'Cloud Computing Engineer',
    'location':'Hyderabad, India', 
    'Salary':'Rs. 20,00,000',
    'skills':'AWS, GCP, Azure',
    'require':'3 yrs+ Experience in Relevant Field'
  },
  {
    'id':4,
    'title':'Data Analyst',
    'location':'Bengaluru, India', 
    'Salary':'Rs. 17,00,000',
    'skills':'SQL, Tableau, Power BI',
    'require':'3 yrs+ Experience in Relevant Field'
  }
]
    
@app.route("/")
def home():
  return render_template("home.html", jobs=JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
