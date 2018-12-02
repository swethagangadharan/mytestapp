from flask import flask,render_template
app=flask(__name__)
@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)
if _name__=='main':
    app.run()