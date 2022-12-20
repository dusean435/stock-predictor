import os
from datetime import datetime
from flask_restx import Namespace, Resource
from flask import current_app as app

prices_ns = Namespace('prices')


@prices_ns.route('/<string:ticker>/historical')
class PricesPredicted(Resource):

  def get(self, ticker):
    try:
      path = os.path.join(app.config['DATADIR'],
                          'historical_prices', ticker + '.csv')
      with open(path, 'r') as f:
        data = [line.split(',') for line in f.readlines()[1:]]
        totimestamp = lambda x: datetime.strptime(x, '%Y/%m/%d').timestamp()
        tofloat = lambda x: float(x)
        data = [[totimestamp(line[0]), *map(tofloat, line[1:])] for line in data]
      return data
    except:
      return None


@prices_ns.route('/<string:ticker>/predicted')
class PricesHistorical(Resource):

  def get(self, ticker):
    try:
      path = os.path.join(app.config['DATADIR'],
                          'predicted_prices', ticker + '.csv')
      with open(path, 'r') as f:
        data = [line.split(',') for line in f.readlines()[1:]]
        totimestamp = lambda x: datetime.strptime(x, '%Y/%m/%d').timestamp()
        tofloat = lambda x: float(x)
        data = [[totimestamp(line[0]), *map(tofloat, line[1:])] for line in data]
      return data
    except:
      return None
