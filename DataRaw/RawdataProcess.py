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


def fullDataSet():
    # df1 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/oil.csv")
    # dfMain = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/TSLA_full.csv")

    # dfMerge = pd.merge(dfMain, df1, how="left")
    # dfMerge.to_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp.csv", index=False)
    dfTemp = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp.csv")
    dfDeath = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/death.csv")
    dfTemp['deaths'] = 0
    #
    for index, row in dfDeath.iterrows():
        print(row[0])
    # dfMerge = pd.concat([dfTemp, dfDeath])
    # print(dfMerge.head())
    # dfTemp.append(dfDeath)
    dfTemp.to_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp2.csv", index=False)

fullDataSet()

