from importlib import import_module
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


MODULES = ['site', 'members']

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()
jwt = JWTManager()


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    jwt.init_app(app)


def register_blueprints(app):
    """ Register all blueprints from modules """
    for module_name in MODULES:
        module = import_module(f'app.{module_name}.routes')
        app.register_blueprint(module.blueprint)


def create_db(app):
    with app.app_context():
        db.create_all()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    register_extensions(app)
    create_db(app)
    register_blueprints(app)

    return app
