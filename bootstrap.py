from flask import Flask ,render_template
app=Flask(__name__)
@app.route('/bootstrap')
def render_static(): 
    page_name="bootstrap"
    
    return render_template("bootstrap.html")
if __name__=='__main__':
    app.run() 
