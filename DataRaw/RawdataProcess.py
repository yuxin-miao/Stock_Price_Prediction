import csv
import pandas as pd
import copy
import numpy as np


def missingValue():
    df_transfer = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_27.csv")
    df_transfer.fillna(0, inplace=True)
    df_transfer.replace(to_replace='', value=0, inplace=True)
    df_transfer.replace(to_replace=' ', value=0, inplace=True)

    # df_transfer = df_transfer[df_transfer['DATE'] > '2010-06-29']
    df_transfer.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_28.csv", index=False)



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
    df1 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/DPRIME2.csv")
    dfMain = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp.csv")
    dfMain.insert(0, column="Date", value=dfMain['DATE'])
    dfMerge = pd.merge(dfMain, df1, how="left")
    dfMerge.to_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp2.csv", index=False)
    # dfTemp = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp.csv")
    # # dateCol = copy.deepcopy(dfTemp["Date"])
    # dfTemp['Date'] = dfTemp['date']
    # dfTemp = dfTemp.set_index("Date")
    # df_transfer = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/DPRIME.csv")
    # dfTemp['DPRIME'] = 0
    # #
    # for index, row in df_transfer.iterrows():
    #     dfTemp.at[row[0], 'DPRIME'] = row[1]
    # dfTemp.reset_index()
    # dateCol = dateCol.tolist()
    # print(dateCol)
    # dfTemp.insert(0, column="Date", value=dateCol)

    # dfMerge = pd.concat([dfTemp, dfDeath])
    # print(dfMerge.head())
    # dfTemp.append(dfDeath)
    # dfTemp.to_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp2.csv", index=False)

def monthlyData():
    df1 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/TOTALSA.csv")
    dfMain = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp2.csv")
    dfMain['TOTALSA'] = 0
    last = 1
    price = 1
    for index, row in df1.iterrows():

        if index == 0:
            last = row[0]
            price = row[1]
            continue

        if row[0] == '2020-10-01':
            dfMain.loc[('2020-09-01' <= dfMain['Date']) & (dfMain['Date'] < '2020-10-01'), 'TOTALSA'] = price / 31.0

            dfMain.loc[('2020-10-01' <= dfMain['Date']) & (dfMain['Date'] < '2020-11-01'), 'TOTALSA'] = row[1] / 31.0
            break
        dfMain.loc[(last <= dfMain['Date']) & (dfMain['Date'] < row[0]), 'TOTALSA'] = price / 30.0
        last = row[0]
        price = row[1]
    dfMain.drop(columns='DATE', inplace=True)
    dfMain.to_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/temp3.csv", index=False)







# fullDataSet()
missingValue()
# monthlyData()