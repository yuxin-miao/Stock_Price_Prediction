rm(list = ls())
install.packages("quantmod")
library(quantmod)
getSymbols("TSLA", src = "yahoo", from = "2020-1-2")
TSLA.full = TSLA
TSLA.full$TSLA.Open

install.packages("forecast")
library(forecast)
model = arima(TSLA.full$TSLA.Open, order = c(10,0,0), method = "ML")
p = predict(model, 9)
result = as.data.frame(p$pred[5:9])

print(result)
write.table(result, file = "./group_3.txt", append = FALSE, quote = FALSE, sep = "\n",
            eol = "\n", na = "NA", dec = ".", row.names = F,
            col.names = F, 
            fileEncoding = "")


