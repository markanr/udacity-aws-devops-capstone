from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello again from app.py! This app for is made the Udacity capstone project of the course \"AWS Cloud DevOps Engineer Nanodegree Program\"'

app.run(host='0.0.0.0', port=80)