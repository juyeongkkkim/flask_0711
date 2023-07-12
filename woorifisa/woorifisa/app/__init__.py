from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy() # CRUD 작업
migrate = Migrate() # db에 관한 수정 사항


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import basic_views, juyeong_views
    app.register_blueprint(basic_views.fisa)
    app.register_blueprint(juyeong_views.juyeong)

    return app