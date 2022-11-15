from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='html')
    app.config['SECRET_KEY'] = "#Laura2001"
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app