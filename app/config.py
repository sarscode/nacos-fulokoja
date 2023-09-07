import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI', f'sqlite:///{os.path.join(BASE_DIR, "db.sqlite3")}')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', None)
    MAIL_SERVER = os.getenv('MAIL_SERVER', None)
    MAIL_PORT = int(os.getenv('MAIL_PORT', '465'))
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', None)
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', None)
    # MAIL_USE_TLS = bool(os.getenv('MAIL_USE_TLS', '')) or False
    MAIL_USE_SSL = bool(os.getenv('MAIL_USE_SSL', 'True')) or True
    SERVER_NAME = os.getenv('SERVER_NAME', None)


class DebugConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_dict = {
    'debug': DebugConfig,
    'production': ProductionConfig
}
