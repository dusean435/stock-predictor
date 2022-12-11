from flask import Flask
from flask_cors import CORS

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(config)

    CORS(app)
    @app.route("/")
    def index():
      return "<h1>*************IT WORKS*************</h1>"


    return app
    