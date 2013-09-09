
from flask import (
    render_template,
    flash,
    redirect,
)

from promlib import app
from promlib.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data +
              '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')

    context = {
        'title': 'Sign In',
        'form': form,
        'providers': app.config['OPENID_PROVIDERS'],
    }
    return render_template('login.html', **context)


@app.route('/')
@app.route('/index')
def index():
    context = {
        'user': 'anonymous',
        'title': 'Sweet home',
    }
    return render_template("index.html", **context)
