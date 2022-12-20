import os
from api.main import create_app

config_path = os.path.join(os.path.dirname(__file__), 'config.py')
app=create_app(config_path)
