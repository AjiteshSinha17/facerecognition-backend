from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes import attendance
    app.register_blueprint(attendance)
    return app
