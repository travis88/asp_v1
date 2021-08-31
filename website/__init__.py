from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate=Migrate()

def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    from website.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    migrate.init_app(app, db)
    
    return app
