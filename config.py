import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Конфиг"""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    """Конфиг для отладки"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data-dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}    
