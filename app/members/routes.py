from threading import Thread
from flask import flash, redirect, render_template, url_for, copy_current_request_context, request
from flask_login import login_user, login_required, logout_user, current_user
from flask_jwt_extended import create_access_token, decode_token
from app import db
from app import login_manager
from app import mail
from app.members import blueprint
from app.members.forms import LoginForm, RegisterForm
from app.members.models import User
from app.members.utils import create_verification_mail, hash_password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) or None


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password = hash_password(form.password.data)
        user = User.query.filter_by(email=form.email_address.data).first()
        if user:
            flash(
                f'We could not created an account for {form.email_address.data}', 'error')
            return redirect(url_for('members_blueprint.register'))

        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    email=form.email_address.data, matric_number=form.matric_number.data, level=form.level.data, password=password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.email_address.data}', 'success')

        verification_token = create_access_token(
            identity=form.email_address.data)

        message = create_verification_mail(
            user.first_name, user.email, verification_token)

        @copy_current_request_context
        def send_message(message):
            mail.send(message)

        email_thread = Thread(
            target=send_message, args=(message,))
        email_thread.start()

        return redirect(url_for('members_blueprint.login'))
    return render_template('site/register.html', form=form)


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('site/login.html', form=form)


@blueprint.route('/email_verification', methods=['GET', 'POST'])
def verify_email():
    token = decode_token(request.args['token'])

    user = User.query.filter_by(email=token['sub']).first()

    if user:
        user.email_verified = True
        db.session.commit()
        flash(
            f'Email verification for {token["sub"]} was successful', 'success')

    return redirect(url_for('members_blueprint.login'))
