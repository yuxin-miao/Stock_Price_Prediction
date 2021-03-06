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


def chooseDate():
    df_transfer = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/scaled_centered.csv")
    df_transfer2 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_30.csv")
    # datetime = pd.to_datetime(dfMain["Date"], dayfirst=True)
    df_transfer.drop(columns='drop', inplace=True)
    # Date = df_transfer2['Date']
    df_transfer.insert(0, column="Date", value=df_transfer2['Date'])
    # df_transfer.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/without_2020.csv", index=False)
    df_transfer.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_31scale.csv", index=False)

def contactDF():
    df1 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/GoogleTrend.csv")
    # df1.reset_index(inplace=True)
    # df2 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/multiTimeline (1).csv",  skiprows=1)
    # df2.reset_index(inplace=True)
    # df3 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/multiTimeline (2).csv",  skiprows=1)
    # df3.reset_index(inplace=True)
    # df4 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/multiTimeline (3).csv",  skiprows=1)
    # df4.reset_index(inplace=True)
    # df = pd.concat([df4, df3, df2, df1])
    # df.drop(columns='index', inplace=True)
    # df.to_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/GoogleTrend.csv", index=False)
    dfMain = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_30.csv")

    # dfMain.insert(0, column="Date", value=dfMain['DATE'])
    dfMerge = pd.merge(dfMain, df1, how="left")
    dfMerge.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_29Google.csv", index=False)




def BrentOil():
    df = pd.read_table('2020Oil.xls')
    print(df.head())
    # df = pd.read_csv('BrentOilPrices.csv', skiprows=5874, names=['Date', 'OilPrice'])
    #
    # datetime = pd.to_datetime(df["Date"], dayfirst=True)
    # df["Date"] = datetime
    # # print(df.head())
    # df.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/oil.csv", index=False)


def death():
    df = pd.read_csv('/Users/yuxinmiao/Desktop/406proj/Dataset/11_30full.csv', usecols=['Date', 'Close'])
    # df.sort_values(by='date', inplace=True)
    df.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/use.csv", index=False)


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

def processCrash():

    dfMain = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/crash.csv", usecols=['Crash Date/Time'])
    dfMain.rename(columns={'Crash Date/Time': 'Date'}, inplace=True)
    datetime = pd.to_datetime(dfMain["Date"], dayfirst=True)
    dfMain["Date"] = datetime
    dfMain = dfMain[dfMain['Date'] > '2020-01-01']

    print(dfMain.head())

def addNew():
    dfMain = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_29Google.csv")
    datetime = pd.to_datetime(dfMain["Date"], dayfirst=True)
    dfMain["Date"] = datetime
    df1 = pd.read_csv("/Users/yuxinmiao/Desktop/406proj/DataRaw/covid-data.csv", usecols=['Date', 'new_cases', 'new_deaths'])
    datetime = pd.to_datetime(df1["Date"], dayfirst=True)
    df1["Date"] = datetime
    dfMerge = pd.merge(dfMain, df1, how="left")
    dfMerge.fillna(0, inplace=True)
    # print(dfMerge.head())

    dfMerge.to_csv("/Users/yuxinmiao/Desktop/406proj/Dataset/11_30full.csv", index=False)

# BrentOil()
# processCrash()
# addNew()
# contactDF()
# chooseDate()
# fullDataSet()
# missingValue()
# monthlyData()
death()