from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/config.js')
def config():
    return app.send_static_file('config.js')

@app.route('/create', methods=['GET'])
def create():
    print(request)
    return 'This is yes.'