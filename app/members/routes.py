from flask import render_template
from app.members import blueprint
from app.members.forms import LoginForm, RegisterForm


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template('site/register.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('site/login.html', form=form)
