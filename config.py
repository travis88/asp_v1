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
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'data-dev.sqlite')}"

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}    
