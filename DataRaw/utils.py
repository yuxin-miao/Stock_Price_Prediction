import datetime
import calendar
import time
import json
import requests
from bs4 import BeautifulSoup


def get_t_str():
    return str(datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]'))


def get_duration(months):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    total = 0

    for i in range(0, months):
        month -= 1
        if month == 0:
            month = 12
            year -= 1
        total += calendar.monthrange(year, month)[1]

    return total


def parse_date(date_str):
    fmt = '%Y-%m-%d'
    time_tuple = time.strptime(date_str, fmt)
    year, month, day = time_tuple[:3]
    return datetime.date(year, month, day)


def parse_content(content, sec):
    # content: pure html text
    # sec: key of json dict
    # used to get all the content in one {}
    keyw = '"{}"'.format(sec)
    tmp = content.find(keyw)

    if tmp == -1:
        return {}

    while content[tmp + len(keyw) + 1] != '{':
        tmp = content.find(keyw, tmp + 1)
        if tmp == -1:
            return {}

    index = tmp + len(keyw) + 2
    count = 1
    str = '{'

    while count > 0:
        if content[index] == '{':
            count += 1
        if content[index] == '}':
            count -= 1
        str += content[index]
        index += 1

    dic = json.loads(str)  # transfer to python dict
    return dic


def get_profile(content):
    profile = parse_content(content, 'summaryProfile')
    type = parse_content(content, 'quoteType')
    sector = profile.get('sector', '')
    exchange = type.get('exchange', '')
    return sector, exchange


def get_financial(symbol):
    # latest_financial = lf
    result = {}
    url = 'https://finance.yahoo.com/quote/{0}/financials?p={0}'.format(symbol)

    # term recorded, annual and quarterly both
    term = {'incomeStatementHistory': ('incomeStatementHistory', 'ISA'),
            'balanceSheetHistory': ('balanceSheetStatements', 'BSA'),
            'cashflowStatementHistory': ('cashflowStatements', 'CFA'),
            'incomeStatementHistoryQuarterly': ('incomeStatementHistory', 'ISQ'),
            'balanceSheetHistoryQuarterly': ('balanceSheetStatements', 'BSQ'),
            'cashflowStatementHistoryQuarterly': ('cashflowStatements', 'CFQ')}

    r = requests.get(url, timeout=45)
    r.raise_for_status()  # raise exception if not 200

    for key, val in term.items():
        temp = parse_content(r.text, key)
        temp = temp.get(val[0], [])
        for item in temp:
            if result.get(item['endDate']['fmt'], None) is None:
                result[item['endDate']['fmt']] = {
                    'ISA': {},
                    'BSA': {},
                    'CFA': {},
                    'ISQ': {},
                    'BSQ': {},
                    'CFQ': {}
                }
            result[item['endDate']['fmt']][val[1]] = item
    return result


def get_statistic(symbol):
    # latest_statistic = ls
    url = 'https://finance.yahoo.com/quote/{0}/key-statistics?p={0}'.format(symbol)
    statistics = 'defaultKeyStatistics'
    r = requests.get(url, timeout=45)
    r.raise_for_status()
    result = parse_content(r.text, statistics)
    return result
    # if result == {}:
    #     return None, ls
    # if datetime.datetime.utcnow().date() > latest_statistic:
    #     return result, datetime.datetime.utcnow().date()
    # else:
    #     return None, datetime.datetime.utcnow().date()

#
# def get_historical(stock, lh=datetime.date(1970, 1, 1), duration=9):
#     latest_historical = lh
#     period2 = int(time.time())
#     period1 = period2 - 86400 * get_duration(duration)
#
#     url = 'https://finance.yahoo.com/quote/{0}/history?period1={1}&period2={2}&interval=1d&filter=history&frequency=1d'.format(
#         stock, period1, period2)
#
#     r = requests.get(url, timeout=45)
#     r.raise_for_status()
#     prices = parse_content(r.text, 'HistoricalPriceStore').get('prices', [])
#     result = []
#
#     # delete dividend data
#     for i in range(len(prices) - 1, -1, -1):
#         if 'type' in prices[i].keys():
#             prices.pop(i)
#         else:
#             date = datetime.date.fromtimestamp(prices[i]['date'])
#             if date > lh:
#                 latest_historical = max(date, latest_historical)
#                 result.append(prices[i])
#
#     if len(result) == 0:
#         result = None
#     return result, latest_historical
