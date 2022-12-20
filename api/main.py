from flask import Flask
from flask_restx import Api
from flask_cors import CORS

from api.stocks import stocks_ns
from api.prices import prices_ns

def create_app(config_path):
    app = Flask(__name__, static_folder='../static')
    app.config.from_pyfile(config_path)

    CORS(app)

    api=Api(app,doc='/docs')
    api.add_namespace(stocks_ns)
    api.add_namespace(prices_ns)

    @app.route("/")
    def index():
        return app.send_static_file('index.html')

    @app.errorhandler(404)
    def not_found(err):
        return app.send_static_file('404.html')

    return app
