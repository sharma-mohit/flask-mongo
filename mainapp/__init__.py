from flask import Flask
from flask.ext.mongoengine import MongoEngine
from pymongo import read_preferences


db = MongoEngine()


def create_app(config=None):
    if not config:
        config = {
            'db': 'testproject',
            'host': '127.0.0.1',
            'port': 27017,
            'read_preference': read_preferences.ReadPreference.PRIMARY,
        }

    app = Flask(__name__)
    app.config["MONGODB_SETTINGS"] = config

    db.init_app(app)

    from api.views import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
