from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/tree')
def tree():
    return 'I am Tree'

