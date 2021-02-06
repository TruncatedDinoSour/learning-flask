from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from os import path

db = SQLAlchemy()
DB_NAME = 'notes_database.db'


def create_app():
    # initialize flask
    app = Flask(__name__)

    # secure the cookies
    app.config['SECRET_KEY'] = 'h3errejse3r47ehj33hdj4453ahkjshker54jerdhjevs'

    # make a database
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_: int):
        return User.query.get(int(id_))

    # import views/routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print(f'Database "{DB_NAME}" created')
