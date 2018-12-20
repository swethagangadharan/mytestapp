from flask import Flask ,render_template, request, session,redirect
from lib import users
import json



app=Flask(__name__)
app.secret_key = 'test'
@app.route('/',methods=['GET','POST'])
def homepage():
    user=users.Users()
    return render_template("homepage.html")


@app.route('/webpage', methods=['GET', 'POST'])
def render_static():
    testSession = session.get('username', None)
    print testSession, "testSession"
    if  request.form:
        name = request.form['name']
        password=request.form['password']
        
       
        if name != "" and password!="":
            user = users.Users()
            user.checkUserLogin(name, password)
            print name, password 
            session["username"] = name
    return render_template("webpage.html")

@app.route('/index',methods=['GET','POST'])
def index():
    user_obj=users.Users()
    return render_template("index.html")

@app.route('/users', methods=['GET', 'POST'])
def render_users():
    user_obj = users.Users()
    all_users = user_obj.getUsers()
    return render_template("users.html", data = all_users)

@app.route('/users/<id>', methods=['GET', 'POST'])
def edit_users(id):
    user_obj = users.Users()
    one_user = user_obj.getUser(id)
    return render_template("edit_users.html", data = one_user)

@app.route('/update_users', methods=['GET','POST'])
def update_users():
    data = request.form
    user_obj = users.Users()
    
    user_obj.updateUser(data)
    one_user = user_obj.getUser(data['id'])
    if 'name' != None and 'password' != None:
            userobj=users.Users()
            return redirect('/users')

    return render_template("edit_users.html", data = one_user)

@app.route('/insertUsers',methods=['GET','POST'])
def insertUsers():
    return render_template("insert_users.html",data={})
    

@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.form:
        name=request.form['name']
        password=request.form['password']
        data=request.form
        userobj=users.Users()
        userobj.insert(data)
        if 'name' != None and 'password' != None:
            userobj=users.Users()
            return redirect('/users')
    return render_template("insert_users.html",data={})  
    
        
   
   
@app.route('/home', methods=['GET', 'POST'])
def home():
    homeSession = session.get('username', None)
    print homeSession, "homeSession"
    return "Hello world"

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session["username"] = None
    
    return render_template("homepage.html")




if __name__=='__main__':
    app.run() 