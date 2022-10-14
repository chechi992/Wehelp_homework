from flask import (
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

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
 

@app.route("/signin",methods = ['POST', 'GET']) #函式的裝飾(Decorator):以函式為基礎，提供附加的功能

def signin():

    if request.method == 'POST':

        session.pop('user',None) #把資料清空

        if request.form['username'] == "" or request.form['password'] == "" :

            return redirect(url_for('error', message='請輸入帳號、密碼')) #在網址列後加入字串

        if request.form['username'] == 'test' and request.form['password'] == 'test':

            session["user"] = request.form['username']

            return redirect(url_for('member'))       

        if request.form['username'] != 'test' or request.form['password'] != 'test':

            return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))
    
    return render_template('login.html')


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
        return redirect(url_for('login')) 

@app.route('/signout')# 登出頁面
def signout():
    session.pop('user',None) # 清空資料
    return redirect(url_for('signin')) 


if __name__ =="__main__":#如果以主程式執行
    app.debug = True
    app.run(port=3000) #立刻啟動伺服器