import csv
import pandas as pd
import numpy as np


def BrentOil():
    df = pd.read_csv('BrentOilPrices.csv', skiprows=5874, names=['Date', 'OilPrice'])

    datetime = pd.to_datetime(df["Date"], dayfirst=True)
    df["Date"] = datetime
    # print(df.head())
    df.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/oil.csv", index=False)


def death():
    df = pd.read_csv('tesla-deaths.csv', usecols=['date', 'deaths'])
    df.sort_values(by='date', inplace=True)
    df.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/death.csv", index=False)


death()