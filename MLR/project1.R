rm(list = ls())
setwd("F:\\FA2020\\VE406\\proj")
## read the data from the website
price = read.csv("TSLA_full.csv", header = T)
price$Date = as.Date(price$Date, format = "%Y-%m-%d")
plot(price$Date, price$Close, col(2), main = "Price vs Date", type = 'l', xlab = "Date", ylab = "Price")
library(ggplot2)
plot(price$Date, price$Close , main = "Price vs Date", xlab = "Date", ylab = "Price", type = 'l', lty = 1)
lines(price$Date, price$Open)

p1 = ggplot(price)+
  geom_line(aes(x = Date, y = Close), color = "black")+
  geom_line(aes(x = Date, y = Open), color = "yellow")+
  geom_line(aes(x = Date, y = High), color = "blue")+
  geom_line(aes(x = Date, y = Low), color = "red")
p1
p2 = ggplot(data = price, geom_line(aes(x = Date, y = Volume), color = "green"))
p2

lm_full = lm(Close ~ Date+Open+High+Low+Volume, data = price)
summary(lm_full)

acf(lm_full$residuals, main = "Error Independence")