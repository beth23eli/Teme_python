from flask import Flask
from .db import init_db
from .routes import solving_bp

def create_app():
    app = Flask(__name__)
    init_db()

    app.register_blueprint(solving_bp, url_prefix="/api")

    return app

