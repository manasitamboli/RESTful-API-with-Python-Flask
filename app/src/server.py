#!flask/bin/python
#!/usr/bin/python
#from src import app
#changed below line
from flask import Flask
from flask import jsonify, abort, request, render_template, json
from flask_cors import CORS
import db


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/users', methods=['GET'])
def get_users():
    data = db.get_users_from_db()
    users1=[]
    for obj in data:
        usr = {'id': obj[0],
        "username": obj[1],
        "displayName": obj[2],
        "department": obj[3]}
        users1.append(usr)
    return jsonify({'users': users1})

@app.route('/users/<string:username>', methods=['GET'])
def get_user(username):
    data = db.get_single_user_from_db(username)
    print data
    if data is None:
        abort(404)
    getuser = [{'id': data[0],
        "username": data[1],
        "displayName": data[2],
        "department": data[3]}]
    print getuser
    return jsonify({'username': getuser[0]})

@app.route('/users/', methods=['POST'])
def create_user():
    request.get_json(force=True)
    if not request.json or not 'username' in request.json or not request.json['username']:
        abort(400)
    if db.get_single_user_from_db(request.json['username']) is not None:
        abort(409)
    else:
        flag = db.add_user_to_db(request.json)
        if flag:
            data = db.get_single_user_from_db(request.json['username'])
            newuser = [{'id': data[0], "username": data[1], "displayName": data[2], "department": data[3]}]
            return jsonify({'newuser': newuser}), 201
        else:
            abort(500)

@app.route('/deleteUser/<string:username>', methods=['GET'])
def delete_user(username):
    data = db.get_single_user_from_db(username)
    print data
    if data is None:
        abort(404)
    else:
        flag = db.delete_user_from_db(username)
        return jsonify({'result': flag})

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
