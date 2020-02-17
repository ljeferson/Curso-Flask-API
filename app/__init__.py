from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Config import config

db = SQLAlchemy()

def crate_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    api = Api(app)
    db.init_app(app)