from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms.validators import DataRequired, Email


class SubscribeForm(FlaskForm):
    email_address = EmailField('Email Address', [DataRequired(
        'Email address is required'), Email('Invalid email address', check_deliverability=True,)])
