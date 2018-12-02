from flask import Flask ,render_template, request
app=Flask(__name__)
@app.route('/index', methods=['GET', 'POST'])
def render_static():
    if  request.form:
        name = request.form['name']
        age = request.form['age']
        password=request.form['password']
        if name != "" and age != "" and password!="":
            print name, age, password
    page_name="index1"  
    return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True) 