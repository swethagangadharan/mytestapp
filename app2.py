from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('',methods=['GET','POST'])
def render_static():
    if request.form:
        