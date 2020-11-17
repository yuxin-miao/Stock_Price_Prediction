import json
import requests
import time
import datetime
import os

from utils import get_financial, get_statistic


# params
class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.exchange = ''
        self.sector = ''
        self.status = 0
        self.latest_financial = datetime.date(1970, 1, 1)
        self.latest_historical = datetime.date(1970, 1, 1)
        self.latest_statistic = datetime.date(1970, 1, 1)
        self.data = {
            "financial": None,
            "statistic": None,
            'historical': None
        }

    def retrieve(self):
        self.data['statistic'] = get_statistic(self.symbol)
        self.data['financial'] = get_financial(self.symbol)
        self.status = 0
        return self

    # Save the result
    def save(self, path='./json'):
        if not os.path.exists(path):
            os.makedirs(path)
        elif not os.path.isdir(path):
            print('Path provided is not a Directory! Check your path!')
            exit(-1)

        filename = '{0} {1}.json'.format(self.symbol, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        with open(os.path.join(path, filename), 'w') as out:
            json.dump({
                'symbol': self.symbol,
                'exchange': self.exchange,
                'sector': self.sector,
                'data': self.data
            }, out)
            print(str(datetime.datetime.now()) + ' Saved {}...'.format(self.symbol))

    def get(self):
        return {
            'symbol': self.symbol,
            'exchange': self.exchange,
            'sector': self.sector,
            'data': self.data
        }


if __name__ == '__main__':
    symbol = 'TSLA'
    tesla_stock = Stock(symbol)
    tesla_stock.retrieve()
    tesla_stock.save()
