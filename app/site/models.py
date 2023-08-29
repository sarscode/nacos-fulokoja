from datetime import datetime
from app import db


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    email_address = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
