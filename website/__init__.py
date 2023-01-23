from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__, template_folder='html')
    app.config['SECRET_KEY'] = "#Laura2001"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}.db'
    db.init_app(app)
    from .views import views
    from .auth import auth
    
    #
    from .models import User, GameHistory
    with app.app_context():
        db.create_all()
        print('Created Database successfully!')
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app