import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    IP_ADDRESS = '180.101.147.89'
    PORT = '8743'
    APP_ID = '4CFpzk3vFme73dJCogtqac6H1EIa'
    SECRET = '6c1qCXEzcp0F0l47iWtvuLYsqlwa'
    CERT = (os.path.join(basedir,'\cert\client.crt'),os.path.join(basedir,'\cert\client.key'))

    @staticmethod
    def __init__app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('')


class ProductConfig(Config):
    DEBUG = False


config = {'develop': DevelopmentConfig,
          'product': ProductConfig}
