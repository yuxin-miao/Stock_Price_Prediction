getwd()
setwd("F:\\FA2020\\VE406\\proj\\ARIMA")
library(forecast)
TSLA.full = read.csv("11_30full.csv", header = T)
TSLA.full$Date = as.Date(TSLA.full$Date, format = "%Y-%m-%d")
close = TSLA.full$Close
plot(TSLA.full$Date, close, type = 'l')

library(leaps)
regsubsets.out = regsubsets(
  Close ~ Volume + OilPrice + deaths + DPRIME + TOTALSA + GoogleTrend + new_cases, data = TSLA.full,
  nbest = 1,
  nvmax = NULL,
  method = "exhaustive"
)
plot(regsubsets.out , scale = "r2", main = "R^2", col = c("darkblue", "blue", "lightblue"))
plot(regsubsets.out , scale = "adjr2", main = "Adjust R^2", col = c("darkgreen","green", "lightgreen"))
plot(regsubsets.out , scale = "Cp", main = " Mallow's Cp ", col = c("orange","yellow", "lightyellow"))
plot(regsubsets.out , main = "BIC", col = c("purple","lightpink", "pink"))


## AR

price = ts(data = TSLA.full$Close[1:202])
plot(price)
acf(price)

auto.arima(price, trace = T)

arima.model = arima(price, order = c(10,0,0), method = "ML")

summary(arima.model)

plot(arima.model$residuals, main = "residuals", lwd = 2, col = "blue", ylab = "residual")

acf(arima.model$residuals,lwd = 3,main = "residuals", col = "blue", ylab = "residual")

qqnorm(arima.model$residuals)
Box.test(arima.model$residuals, type = "Ljung-Box")
pred = predict(arima.model, 20)
plot(pred$pred, xlim = c(100,222), lwd = 3, col =rgb( 0, 0, 1,1), main = "prediction for AR",
     xlab = "time index", ylab = "price", ylim= c(200,500))
lines(TSLA.full$Close, col = rgb(1, 0 ,0,0.6), lwd = 3)

legend("bottomright", legend = c("training set", "testset"), col = c("red", "blue"),
       lty = 1, lwd = 2)

pred$pred
score = sum((TSLA.full$Close[203:222]-pred$pred)^2)
score





library(xts)
close.ts = xts(TSLA.full[], TSLA.full$Date)
TSLA.full.lm = lm(Close ~ OilPrice + DPRIME + TOTALSA + GoogleTrend
                  + new_cases, data = TSLA.full)
summary(TSLA.full.lm)
plot(TSLA.full.lm, which = 1, pch = 1, lwd = 2)
acf(TSLA.full.lm$residuals, main = "acf plot")
pacf(TSLA.full.lm$residuals, main = "pacf plot")

TSLA.full.lm = lm(Close ~ OilPrice + DPRIME + TOTALSA + GoogleTrend
                  + new_cases, data = TSLA.full)
summary(TSLA.full.lm)
plot(TSLA.full.lm, which = 1, pch = 16, lwd = 3, col= "blue")
plot(TSLA.full.lm$residuals, xlab = "time" , ylab = "residuals", main = "residuals plot", 
     pch = 16, col = "blue" )
abline(a = 0, b = 0, col = "red", lwd = 3)
acf(TSLA.full.lm$residuals, main = "acf plot", col = "blue", lwd = 2)
pacf(TSLA.full.lm$residuals, main = "pacf plot",col = "blue", lwd = 2)

arima.model = arima(TSLA.full.lm$residuals, order = c(10,1,1))
summary(arima.model)

model = arima(TSLA.full$Close,xreg = cbind(o = TSLA.full$OilPrice,
                                                d = TSLA.full$DPRIME,
                                                t = TSLA.full$TOTALSA,
                                                g = TSLA.full$GoogleTrend,
                                                n = TSLA.full$new_cases) , 
              order = c(10,1,0))
model
plot(model$residuals, ylab = "residuals", lwd = 2, col = "blue", main = "residuals")
abline(a = 0, b = 0, col = "red", lwd = 2)
acf(model$residuals, main = "acf plot", lwd = 3, col = "blue")
pacf(model$residuals, main = "pacf plot")
tsdiag(model)

model$sigma2
model$coef
nrow(TSLA.full)
p = predict(model, newxreg = cbind(o = TSLA.full$OilPrice[200:222],
                                   d = TSLA.full$DPRIME[200:222],
                                   t = TSLA.full$TOTALSA[200:222],
                                   g = TSLA.full$GoogleTrend[200:222],
                                   n = TSLA.full$new_cases[200:222]), ahead = 44)
plot(TSLA.full$Close, xlim = c(100,240), type = 'l', col = 'red', lwd = 2)
lines(p$pred, col = 'blue', lwd = 2)
p$pred


trainset = TSLA.full[1:202,1:13]
model2 = arima(trainset$Close,xreg = cbind(o = trainset$OilPrice,
                                           d = trainset$DPRIME,
                                           t = trainset$TOTALSA,
                                           g = trainset$GoogleTrend,
                                           n = trainset$new_cases) , 
              order = c(10,1,0))
summary(model2)
p2 = predict(model2, newxreg = cbind(o = TSLA.full$OilPrice[202:222],
                                     d = TSLA.full$DPRIME[202:222],
                                     t = TSLA.full$TOTALSA[202:222],
                                     g = TSLA.full$GoogleTrend[202:222],
                                     n = TSLA.full$new_cases[202:222]))
p2$pred
plot(trainset$Close, xlim = c(100,230), type = 'l', col = 'red',
     ylab = "close",
     main = "prediction vs real", lwd = 3)
lines(p2$pred, col = "blue" , lwd = 3)
lines(c(202:222),TSLA.full$Close[202:222],col = "red", lwd = 3)

legend("bottomright", legend = c("training set", "testset"), col = c("red", "blue"),
       lty = 1, lwd = 2)

score = sum((TSLA.full$Close[202:222]-p2$pred)^2)
score

## garch

library(forecast)
TSLA.full = read.csv("11_30full.csv", header = T)
TSLA.full
TSLA.full$Date = as.Date(TSLA.full$Date, format = "%Y-%m-%d")
library(xts)
x = xts(TSLA.full$Close[1:202], TSLA.full$Date[1:202])
TSLA.ts = ts(x)
pacf((TSLA.full$Close[1:202]-mean(TSLA.full$Close)^2), main = "pacf" , col = "blue", lwd = 3)

Box.test((TSLA.full$Close[1:202]-mean(TSLA.full$Close))^2, 
         lag=12, type="Ljung")

library(fGarch, quietly = TRUE)
mod1 <- garchFit( ~  1 +  garch(1,1), data=TSLA.ts, trace=T)
summary(mod1)
residuals(mod1)
plot(mod1, main= "residuals", lwd = 3, which = 9 )
predict(mod1, 10)

## var


library(MTS, quietly = TRUE)
z = coredata(x)
z
varmodel = MTS::VAR(z,1)
varmodel = MTS::VAR(z,2)
m3 = VARorder(z)
plot(m3$aic, xlab = "p", ylab = "AIC", col = "blue", lwd = 2, type = "l", main = "AIC with different p")
plot(varmodel$residuals, main = "residuals", ylab = "residual")
summary(varmodel)
VARpred(varmodel,20)

## data split

x = xts(TSLA.full[2:5], TSLA.full$Date)
x = x[1:202]
z = coredata(x)
varmodel2 = MTS::VAR(z,2)
plot(varmodel2$residuals, main = "residuals", ylab = "residual")
p3 = VARpred(varmodel2,20)

p3$pred[,4]
plot(TSLA.full$Close, xlim = c(100,222), type = 'l', col = 'red', lwd = 2, main = "price prediction", ylab = "price")
lines(c(203:222), p3$pred[,4], col = 'blue', lwd = 2)
legend("bottomright", legend = c("training set", "testset"), col = c("red", "blue"),
       lty = 1, lwd = 2)

score = sum((TSLA.full$Close[203:222]- p3$pred[,4])^2)
score
