from flask import Flask
from .controllers.operationController import OperationController
from .extensions import db, migrate
from dotenv import load_dotenv
load_dotenv()


def create_app():
    app = Flask(__name__)
    #app.config.from_object("config.Config")
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    operation_controller = OperationController()
    app.register_blueprint(operation_controller.blueprint)

    return app

