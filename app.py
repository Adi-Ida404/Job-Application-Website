from flask import Flask, jsonify, render_template
from database import load_job_from_db

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
    'Salary':'$ 500,000',
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

@app.route("/jobs/<id>")
def show_job(id):
  job = load_job_from_db(id)
  return render_template("jobpage.html", job=job)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
