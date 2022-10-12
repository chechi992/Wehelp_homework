from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

class User:
    def __init__(self,id,username,password) :
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User:{self.username}>'    

users = []
users.append(User(id=1,username = 'test',password='test'))

app = Flask(__name__,template_folder='./templates',static_url_path='/static') #__name__代表目前執行的模組

app.config['SECRET_KEY'] = 'Your Key'

@app.route("/",methods = ['POST', 'GET']) #函式的裝飾(Decorator):以函式為基礎，提供附加的功能

def login():

    if request.method == 'POST':
        session.pop('user',None)

        if request.form['username'] == "" or request.form['password'] == "" :

            return redirect(url_for('fail', message='請輸入帳號、密碼'))

        if request.form['username'] == 'test' and request.form['password'] == 'test':

            session["user"] = request.form['username']

            return redirect(url_for('profile'))       

        if request.form['username'] != 'test' or request.form['password'] != 'test':

            return redirect(url_for('fail', message='帳號、或密碼輸入錯誤'))
    
    return render_template('login.html')

@app.route("/fail") 
def fail():

    message = request.args['message']
    print(message)
    return render_template('fail.html', message = message) #傳遞參數

@app.route("/profile") #代表我們要處理的網站路徑
def profile():
    if "user" in session:
        user = session['user']
        return render_template('profile.html')
    else:
        return redirect(url_for('login')) 

@app.route('/signout')# 登出頁面
def signout():
    session.pop('user',None)
    return redirect(url_for('login')) 


if __name__ =="__main__":#如果以主程式執行
    app.debug = True
    app.run() #立刻啟動伺服器