import os
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp

EMAIL_REGEXP = "[a-zA-Z0-9]*@(gmail|yopmail).com" if os.getenv('DEBUG') == 'True' or os.getenv(
    'FLASK_ENV') != 'development' else "[a-zA-Z0-9]*@fulokoja.edu.ng"


class RegisterForm(FlaskForm):
    first_name = StringField(
        'First Name', [DataRequired('First Name is required')])
    last_name = StringField('Last Name', [
                            DataRequired('Last Name is required')])
    email_address = EmailField('Email Address', [DataRequired(
        'Email address is required'), Email('Invalid email address', check_deliverability=True), Regexp(EMAIL_REGEXP, message='Not a student email')])
    matric_number = StringField(
        'Matric Number', [DataRequired('Matric Number is required'), Regexp("[sci]{3}[1-9]{2}[csc]{3}[1-9]{3}")])
    level = SelectField(label='Current Level', choices=[(
        100, '100 Level'), (200, '200 Level'), (300, '300 Level'), (400, '400 Level')])
    password = PasswordField('Password', [DataRequired('Password is required'), Length(
        min=6, message='Password must not be less than  characters')])


class LoginForm(FlaskForm):
    email_address = EmailField('Email Address', [DataRequired(
        'Email address is required'), Email('Invalid email address', check_deliverability=True), Regexp(EMAIL_REGEXP, message='Not a student email')])
    password = PasswordField('Password', [DataRequired('Password is required'), Length(
        min=6, message='Password must not be less than  characters')])
