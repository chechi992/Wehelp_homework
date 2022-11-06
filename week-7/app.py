
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
    jsonify,
    make_response
)

import sqlite3


from flaskext.mysql import MySQL

import pymysql
import mysql.connector
 
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
database="website"
)

#windows : password="1234"

cursor = db.cursor()


class User: #定義user
    def __init__(self,id,username,password) :
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self): # f-string(格式化字串常數) 類似JS的${}
        return f'<User:{self.username}>'    

users = []
users.append(User(id=1,username = 'test',password='test')) #設定登入帳號密碼

app = Flask(__name__,template_folder='./templates',static_url_path='/static') #__name__代表目前執行的模組

app.config['SECRET_KEY'] = 'Your Key' #session 需設定 secret-key

@app.route("/") #函式的裝飾(Decorator):以函式為基礎，提供附加的功能

def home():
    
    return render_template('login.html')



@app.route('/api/member/all', methods=['GET'])
def api_all():
   
    query_parameters = request.args

    id = query_parameters.get('id')

    query = "SELECT * FROM accounts "
    to_filter = []

    cursor.execute(query, to_filter)
    results = cursor.fetchall()

    return jsonify(results)

@app.route('/api/member', methods=['PATCH'])
def update():
    
    req = request.get_json()
    print(req)

    res = make_response(jsonify({"name":req}),200)

    return res

@app.route('/api/member', methods=['GET'])
def api_id():

    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.

    if 'username' in request.args:
        username = str(request.args['username'])
        sql = "SELECT id, name,username FROM accounts WHERE username = %s"
        valid = (username,)
        cursor.execute(sql,valid)
        data = cursor.fetchone()
        null = None
        if data :
            result = {'id':data[0],'name':data[1],'username':data[2]}
            return jsonify({'data':result}),200
        else:
            return jsonify({'data':null})
        
    return render_template('member.html')
   

@app.route("/signup",methods = ['POST', 'GET'])

def signup():

    message = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
   
  #Check if account exists using MySQL
        query = 'SELECT * FROM accounts WHERE username = %s'
        valid = (username,)
        cursor.execute(query,valid)
        account = cursor.fetchone() #抓取一筆資料
        if account:
            
            return redirect(url_for('error', message='帳號已經被註冊'))#傳遞參數

        else:

            #建立資料
            sql = 'INSERT INTO accounts VALUES (NULL,%s, %s, %s)' 
            val = (name, username, password,)
            cursor.execute(sql, val) 
            db.commit()
   

    return render_template('member.html')
  

@app.route("/signin",methods = ['POST', 'GET']) #函式的裝飾(Decorator):以函式為基礎，提供附加的功能

def signin():

  
    if request.method == 'POST' :

        session.pop('username',None)
        username = request.form['username']
        password = request.form['password']
        
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        record = cursor.fetchone()
        db.commit()

        if record : #確認record是否存在
            #創建session
            session['loggedin'] = True
            session['username'] = record[2]
            session['password'] = record[3]
            session['name']=record[1]
            return redirect(url_for('member'))

        else:
            #帳號不存在或輸入錯誤
            return redirect(url_for('error', message='帳號或密碼輸入錯誤'))
    
    return render_template('login.html')


@app.route("/error") 
def error():

    message = request.args['message'] # query-string
    return render_template('error.html', message = message) #傳遞參數

@app.route("/member") #代表我們要處理的網站路徑
def member():

    
    if "username" in session:
        username = session['username']
        return render_template('member.html')
    else:
        return redirect(url_for('home')) 

@app.route('/signout')# 登出頁面
def signout():
    session.pop('username',None) # 清空資料
    return redirect(url_for('home')) 


if __name__ =="__main__":#如果以主程式執行
    app.debug = True
    app.run(port=3000) #立刻啟動伺服器