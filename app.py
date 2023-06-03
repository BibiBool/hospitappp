from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'India',
    'salary': '$ 55,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'California, USA',
  },
  {
    'id': 3,
    'title': 'Data Engineer',
    'location': 'Canada',
    'salary': '$ 75,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)