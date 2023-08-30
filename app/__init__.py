from importlib import import_module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


MODULES = ['site', 'members']

db = SQLAlchemy()
migrate = Migrate()


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)


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
