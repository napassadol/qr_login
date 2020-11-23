from flask import Flask, render_template, request, session, redirect, url_for, escape, abort, jsonify, send_file, send_from_directory
import json
import mysql.connector
from MysqlWrapper import MySQLWrapper


app = Flask(__name__, static_url_path='', static_folder="static")
app.secret_key = 'qrcode'

mysql = MySQLWrapper(
    host="128.199.235.198",
    user="qrlogin",
    passwd="12341234",
    database="qr_login"
)

@app.route('/')
def hello():    
    return render_template('index.html')

@app.route('/register')
def register():    
    return render_template('register.html')

@app.route('/room')
def room():
    if(session.get('username', None) != None):
        return render_template('room.html')
    else:
        return render_template('index.html')

@app.route('/edit_room')
def edit_room():
    if(session.get('admin', False) == True):
        return render_template('edit_room.html')
    else:
        return render_template('index.html')

@app.route('/logout', methods=["POST"])
def logout():
    session['username'] = None
    session['admin'] = False
    return 'ok'

@app.route('/check_admin', methods=["POST"])
def check_admin():
    return jsonify({
        'admin': session.get("admin", False)
    })

@app.route('/send_register', methods=["POST"])
def send_register():
    global mysql
    requestData = json.loads(request.data)
    rowId = mysql.register(requestData)
    return jsonify({'id': rowId})

@app.route('/login', methods=["POST"])
def login():
    global mysql
    requestData = json.loads(request.data)
    user, status = mysql.login(requestData)
    session['username'] = user.get('username', None)
    session['admin'] = user.get('admin', False)
    return jsonify({
        'user': user,
        'status': status
        })
    
if __name__ == '__main__':    
    app.run(debug=True)