from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/webpage', methods=['GET', 'POST'])

def render_static():
    if  request.form:
        name = request.form['name']
        password= request.form['password']
        
        if name != "" and password != "":
            print name, password 
    return render_template("webpage.html")


if __name__=='__main__':
    app.run(debug=True) 