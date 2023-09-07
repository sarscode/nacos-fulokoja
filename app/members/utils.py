from app import bcrypt
from flask_mail import Message
from flask import current_app, url_for


def hash_password(password):
    """Hash user password
    Args:
        password (str): Hashed password
    Returns:
        str: Hashed password
    """
    return bcrypt.generate_password_hash(password).decode("utf-8")


def verify_password(hashed_password, password):
    return bcrypt.check_password_hash(hashed_password, password)


def create_verification_mail(first_name, email_address, verification_token):
    verification_link = f"http://{current_app.config['SERVER_NAME']}{url_for('members_blueprint.verify_email', token=verification_token)}"

    html = f"""
            <h2>Confirm your email address</h2>
            <p>Hello, {first_name}.</p>
            <p>Thank you for signing up to NACOS Fulokoja Chapter</p>
            <p>Please <a href="{verification_link}" target="_blank">confirm your email address</a> to complete your signup.</p>
            <p>If you have any complaints, please reach out to {current_app.config['MAIL_USERNAME']}</p>
            """
    msg = Message(subject='Confirm your email address', recipients=[
        email_address], html=html, sender=("NACOS Fulokoja Chapter", "salifusanirich@gmail.com"))
    return msg


def create_password_reset_mail(first_name, email_address, reset_token):
    reset_link = f"http://{current_app.config['SERVER_NAME']}{url_for('members_blueprint.reset_password', token=reset_token)}"

    html = f"""
            <h2>Reset your password</h2>
            <p>Hello, {first_name}.</p>
            <p>Your requested to change your password</p>
            <p>Here is <a href="{reset_link}" target="_blank">your password reset link</a></p>
            <p>If you have any complaints or you didn't request to reset your password, please reach out to {current_app.config['MAIL_USERNAME']}</p>
            """
    msg = Message(subject='Reset your password', recipients=[
        email_address], html=html, sender=("NACOS Fulokoja Chapter", "salifusanirich@gmail.com"))
    return msg
