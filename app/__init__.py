import os
from flask import Flask
from flask_cors import CORS


def create_app(config):
    os.makedirs(f'{config.BASEDIR}/data/historical_prices', exist_ok=True)
    os.makedirs(f'{config.BASEDIR}/data/predicted_prices', exist_ok=True)

    app = Flask(__name__, static_folder='../static')
    app.config.from_object(config)

    CORS(app)

    @app.route("/")
    def index():
        return app.send_static_file('index.html')

    @app.errorhandler(404)
    def not_found(err):
        return app.send_static_file('404.html')

    return app
