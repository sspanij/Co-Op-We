from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
    {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Bengaluru, India',
    'salary': 'Rs 10,00,000',
    },
    {
    'id' : 2,
    'title' : 'Data Scientist',
    'location' : 'Delhi, India',
    'salary': 'Rs 15,00,000',
    },
    {
    'id' : 3,
    'title' : 'Front-End Developer',
    'location' : 'SanFranciso, USA'
    },
    {
    'id' : 1,
    'title' : 'Back-End Developer',
    'location' : 'Hyderabad, India',
    'salary': 'Rs 12,00,000',
    }
 ]

@app.route('/')
def hello_COW():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/courses')
def course():
    return render_template('courses.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)