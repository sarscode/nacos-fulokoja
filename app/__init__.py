from importlib import import_module
from flask import Flask


MODULES = ['site']


def register_blueprints(app):
    """ Register all blueprints from modules """
    for module_name in MODULES:
        module = import_module(f'app.{module_name}.routes')
        app.register_blueprint(module.blueprint)


def create_app(config_dict):
    app = Flask(__name__)
    app.config.from_object(config_dict)

    register_blueprints(app)

    return app
