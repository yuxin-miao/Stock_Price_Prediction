# Tesla Stock Price Prediction



## Pre-Data Analysis

### Analyze *Close* Price with *Date​* as a Univariate Time Series

As our goal is to predict the stock *close* price, we decide to analyze the features of *close* variable first.



> The following plots implemented in “full_data_outliers.ipynb”

### Moving Average and Smooth

To reduce the effect of noise and have a better understanding of underlying trend, we may use moving average and smooth to visualize the data. 

- Moving average with rolling = 7, 15, 30 respectively 

![image-20201129152911108](/Users/yuxinmiao/Desktop/406proj/x2.png)

​		We could see the moving average is highly similar to the original data. 

- Smooth 

![image-20201129153441194](/Users/yuxinmiao/Desktop/406proj/x3.png)

​		The overall trend is increasing and for each method, in year 2020, there is a sharp increase and the trend in the previous year might not be appropriate to predict the stock price in 2020. So we determine to further examine this problem.



#### Correlation 

For time series data, it has high probability of correlation in itself. So we get the *Close* price after shifting $x$ days, denoted as $Close_x$. And plot $Close_x$ vs. $Close$ to see if there is correlation. 

<img src="./Analysis/x.png" alt="image-20201129151954242" style="zoom:110%;" />

Observe that at the previous years, the data has more correlation. While the latest few years the data scatter more. No obvious difference when using different $x$ days. 

<img src="./Analysis/x1.png" alt="image-20201129152348239" style="zoom:80%;" />

And we use ACF plot to see 

> TODO

 





Combine with the moving average, we get the plot and the correlated score is calculated through method pearson : standard correlation coefficient

<img src="./Analysis/correlation.png" alt="image-20201129152348239" style="zoom:80%;" />

Observe that the *Close* price is highly correlated to other effects 



### Year Trend and Seasonality

<img src="./Analysis/x4.png" alt="image-20201129153441194" style="zoom:110%;" />

From the plot, we could cearly observe that year 2020 has extremely different values compared to other years. We exclude year 2020 to see the trend.

<img src="./Analysis/x5.png" alt="image-20201129153441194" style="zoom:110%;" />

It clearly shows the previous outliers in the month-wise plot is caused by year 2020 and no seasonality exists. Also, the year-wise plot suggests that no cyclic relation exists, and it might be better to use only year 2020 data to predict the stock price. 



### Outliers

To observe the outliers, we decide to use all of the previous introduced variables (moving average and shifted close values) and use K-means cluster to fit a simple model. We decide to choose among `n_cluster=range(1,30)` and use the score to choose the number. 

> we do not want to use these models as a fit model, just to analyze the data. So no checking for any assumptions as a Machine learning manner. 

<img src="./Analysis/x6.png" alt="image-20201129153441194" style="zoom:80%;" />

So we choose number=10 and observe the outliers, where we define the points' $|distance|$ is in the largest $10\%$ as outlier. $distance=predict-observed \ value$

<img src="./Analysis/dis1.png" alt="image-20201129153441194" style="zoom:120%;" />

Nearly all of the points in year 2020 are considered as outliers, so year 2020 might be better not to predicted using all of the data. 

Where the same situations for 

- IsolationForest

<img src="./Analysis/dis2.png" alt="image-20201129153441194" style="zoom:120%;" />

- OneClassSVM

<img src="./Analysis/dis3.png" alt="image-20201129153441194" style="zoom:120%;" />

- EllipticEnvelope

<img src="./Analysis/dis4.png" alt="image-20201129153441194" style="zoom:120%;" />

Therefore, we decide to analyze year 2020 only 

> The following plots implemented in “2020_data_outliers.ipynb”

// TODO 不太确定需不需要





## Data collecting

- Search and Choose possibly useful data

  We intend to choose data from different categories, to prevent data used repeatedly. However, there must exhibt correlation among collected data. 

- //TODO 

  //需要解释每个data含义的table

### Collected Data Analysis

- **Correlation between predictors**. We use $Pearson$ correlation to measure the correlation between predictors 

  <img src="./Analysis/pred1.png" alt="image-20201129153441194" style="zoom:120%;" />

  - correlation = 1 for *Open*, *High*, *Low* prices, as expected.
  - // 我不知道多大算大诶!!
  - *Volume* has a bit high correlation with *DPRIME* and *TOTALSA* (0.45 and 0.36) respectively. 
  - *OilPrice* has rather high correlation with *DPRIME* and *TOTALSA* (0.64 and 0.82) respectively

  This predictors correlated problem will be discussed later. 

- **Collected data as time series**. The predictor itself could be considered as time series. We need to examine its properties and discuss potential issue of using time series to predict a time series.

  - //TODO: time series property 

  - **Granger causality test**  Use time series to predict a time series. We use this statistical hypothesis to 

  - 

  - 

    

We regularized the data







# Model

## With only year 2020 Close data



### Analysis based on year 2020 data

> Another notebook

<img src="./Analysis/1.png" alt="image-20201129153441194" style="zoom:120%;" />



#### Decomposition

<img src="./Analysis/2.png" alt="image-20201129153441194" style="zoom:120%;" />\

Observe that 

- it basically follows an increasing trend
- some fluctuations and sharp decrease / increase residual exists 





**20% test data**, we can’t use cross-validation for this time series, 

MODELS 

## AR



## MA 



## ARIMA







> in analysis.ipynb

**Exponential**

Specifically, past observations are weighted with a geometrically decreasing ratio.

## Simple Exponential Smoothing (SES)

The method is suitable for univariate time series without trend and seasonal components. 

<img src="./Analysis/SES1.png" alt="image-20201129153441194" style="zoom:120%;" />

## Holt’s Method

<img src="./Analysis/holt.png" alt="image-20201129153441194" style="zoom:120%;" />





### Holt-Winter (HWES)

With a constant seasonality component along with an increasing trend, we may try  **Holt-Winter additive model** 

<img src="./Analysis/wint2.png" alt="image-20201129153441194" style="zoom:120%;" />

<img src="./Analysis/wint3.png" alt="image-20201129153441194" style="zoom:120%;" />



Train test spilt with  training set and 20 test set 

### SARIMA

<img src="./Analysis/sarima.png" alt="image-20201129153441194" style="zoom:120%;" />



## VAR for multivariate time series

