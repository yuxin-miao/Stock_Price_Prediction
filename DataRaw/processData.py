import json
import csv
import pandas as pd
import numpy as np

json_data = open('./json/TSLA 2020-11-17 16:04:49.json').read()
data = json.loads(json_data)['data']
financial_data = data['financial']
statistic_data = data['statistic']

'''Process financial data from yahoo finance'''
term = []
for key, value in financial_data['2019-12-31'].items():
    for k0, v0 in value.items():
        term.extend(list(value.keys()))
print(term)
#
# statistic_field = list(statistic_data.keys())
# # print(statistic_field)
# with open('yahoo_statistic.csv', 'w+') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=statistic_field)
#     writer.writeheader()
#     writer.writerows(statistic_data)
#
# for k, v in data.items():
#     print(k + ':' + str(v))
