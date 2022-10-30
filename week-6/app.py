
from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)


from flaskext.mysql import MySQL

import pymysql 
import mysql.connector
 
db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
database="website"
)

cursor = db.cursor()


# # sign up
# cursor.execute("SELECT * FROM member")
# results = cursor.fetchall()
# print(results)

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
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'website'

# mysql = MySQL(app)

@app.route("/") #函式的裝飾(Decorator):以函式為基礎，提供附加的功能

def home():
    
    return render_template('login.html')

@app.route("/signup",methods = ['POST', 'GET'])

def signup():

    # connect
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="website"
    )

    cursor = db.cursor()
   
    # Output message if something goes wrong...
    message = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
        # Create variables for easy access
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
   
  #Check if account exists using MySQL
        query = 'SELECT * FROM accounts WHERE username = %s'
        valid = (username,)
        cursor.execute(query,valid)
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            
            return redirect(url_for('error', message='帳號已經被註冊'))#傳遞參數

        else:

            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            sql = 'INSERT INTO accounts VALUES (NULL,%s, %s, %s)' 
            val = (name, username, password,)
            cursor.execute(sql, val) 
            db.commit()
   
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('member.html', msg=msg)
  

@app.route("/login",methods = ['POST', 'GET']) #函式的裝飾(Decorator):以函式為基礎，提供附加的功能

def login():

 # connect
    
    # connect
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="website"
    )

    cursor = db.cursor()

  
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        
   
    # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            # Redirect to home page
            #return 'Logged in successfully!'
            return redirect(url_for('member'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    
    return render_template('login.html', msg=msg)


@app.route("/error") 
def error():

    message = request.args['message'] # query-string
    return render_template('error.html', message = message) #傳遞參數

@app.route("/member") #代表我們要處理的網站路徑
def member():
    if "user" in session:
        user = session['user']
        return render_template('member.html')
    else:
        return redirect(url_for('home')) 

@app.route('/signout')# 登出頁面
def signout():
    session.pop('user',None) # 清空資料
    return redirect(url_for('home')) 


if __name__ =="__main__":#如果以主程式執行
    app.debug = True
    app.run(port=3000) #立刻啟動伺服器