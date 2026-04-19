from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name='development'):
    app = Flask(__name__)

    from app.config import config_by_name
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes.api import api_bp
    from app.routes.web import web_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(web_bp)

    return app
