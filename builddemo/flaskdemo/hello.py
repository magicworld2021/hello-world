from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app,resources=r'/*')

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api',methods={'POST'})
def houtai_post():
    return 'post sucess!'

if __name__=='__main__':
    app.run(host='0.0.0.0',port='5000')


