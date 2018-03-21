'''
Routes of the flask app.
'''

from flask import Flask, request, make_response
from project.process import *
import json

app = Flask(__name__)

def pack(data):
    re = make_response(data)
    re.mimetype = 'application/json'
    return re

@app.route('/api/login', methods = ['GET'])
def api_login_get(): # Show a simple page for user login
    return '''
           <html>
             <head>
               <title>Project Login</title>
             </head>
             <body>
               <form action="/api/login" method="post">
                 <p>Username: </p><input type="text" name="username"></input>
                 <p>Password: </p><input type="password" name="password"></input>
                 <input type="hidden" name="test" value="1">
                 <input type="submit" value="Login">
               </form>
             </body>
           </html>
           '''

@app.route('/api/login', methods = ['POST'])
def api_login_post(): # Receive user's info and return corresponding token 
    if request.form.get('test') == '1':
        data = request.form.to_dict()
    else:
        data = json.loads(request.data)
    return pack(json.dumps(GetAuth(data['username'], data['password'])))

@app.route('/api/lib', methods = ['GET', 'POST'])
def api_lib_get(): # Get the result page of the books
    page = 1
    if request.method == 'GET':
        title = request.args.get('title')
        if request.args.get('page'):
            page = request.args.get('page')
    elif request.method == 'POST':
        data = json.loads(request.data)
        title = data.get('title')
        if 'page' in title:
            page = data.get('page')
    if not title:
        return 'Error: No book title specified. Please check your request.'
    return pack(json.dumps(GetBookList(title, page)))
