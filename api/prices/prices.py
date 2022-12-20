import os
from flask_restx import Namespace, Resource
from flask import current_app as app

prices_ns = Namespace('prices')

@prices_ns.route('/<string:ticker>/historical')
class PricesPredicted(Resource):

  def get(self, ticker):
    try:
      path = os.path.join(app.config['DATADIR'], 'historical_prices', ticker + '.csv')
      with open(path, 'r') as f:
        return f.read()
    except:
      return None

@prices_ns.route('/<string:ticker>/predicted')
class PricesHistorical(Resource):

  def get(self, ticker):
    try:
      path = os.path.join(app.config['DATADIR'], 'predicted_prices', ticker + '.csv')
      with open(path, 'r') as f:
        return f.read()
    except:
      return None