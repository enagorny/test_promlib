
from flask import render_template


from promlib import app

@app.route('/')
@app.route('/index')
def index():
    context = {
        'user': 'anonymous',
        'title': 'Sweet home',
    }
    return render_template("index.html", **context)
