import re
from flask_restx import Namespace, Resource, reqparse
from api.companies import companies

stocks_ns = Namespace('stocks')

@stocks_ns.route('/')
class Stocks(Resource):

  def get(self):
    return companies

@stocks_ns.route('/<string:ticker>/info')
class StocksInfo(Resource):

  def get(self, ticker):
    # TODO: Implement a way to get the stock info for a specific company like market cap, IPO date, etc.
    info = filter(lambda x: x['ticker'] == ticker, companies)
    return list(info)

@stocks_ns.route('/search')
class StocksSearch(Resource):

  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('q', type=str, help='Ticker symbol or name of the company.')
    args = parser.parse_args()
    
    if args.get('q'):
      q = args.get('q').lower()
      search = lambda x: re.search(q, x['ticker'].lower()) or re.search(q, x['company'].lower())
      results = filter(search, companies)
      return list(results)
    
    return companies
    
    