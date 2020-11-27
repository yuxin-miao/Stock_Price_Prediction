## RAWDATA

### Final Dataset

each file corresponding columns in 11_27.csv

| oil.csv         | death.csv     | DPRIME.csv   | TOTALSA.csv                                            |      |      |      |      |
| --------------- | ------------- | ------------ | ------------------------------------------------------ | ---- | ---- | ---- | ---- |
| OilPrice, daily | Deaths, daily | DPRIME daily | TOTALSA monthly data divided by 30, assgin to each day |      |      |      |      |



1. *oil.csv:* daily oil price, in USD.

   > Dataset is available on U.S. Energy Information Administration: [Europe Brent Spot Price FOB (Dollars per Barrel)](https://www.eia.gov/dnav/pet/hist_xls/RBRTEd.xls) which is updated on weekly bases.
2. Google Search Trend: in DataRaw/multitimeline.csv, could be more detailed
3. GDP: each year's data in DataRaw
4. *death.csv*: death people number caused by Tesla, raw data in tesla-deaths.csv
5. *TOTALSA.csv*: Total mobile sales, data collected monthly
6. *DPRIME.csv*: Bank Prime Loan Rate, data collected daily, some missing data **set as 0**

长线比如GDP，销量什么的，一个fit用，predict似乎没用

