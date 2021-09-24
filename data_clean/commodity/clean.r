library(lubridate)
library(dplyr)
setwd("D:/PycharmProjects/GU-ANLY-501-FALL-2021/data_gather/commodity/data")

# clean aluminum data
al = read.csv("Aluminum.csv")
str(al)
al$Date = as.Date(al$Date)
str(al)
al = al[year(al$Date) >= 2015,c("Date", "Close")]
al$Close = as.numeric(al$Close)
sum(is.na(al$Close))
which(is.na(al$Close))
al = na.omit(al)
summary(al$Close)
colnames(al)[2] = "aluminum"
colnames(al)

# clean copper data
cu = read.csv("Copper.csv")
str(cu)
cu$Date = as.Date(cu$Date)
str(cu)
cu = cu[year(cu$Date) >= 2015,c("Date", "Close")]
cu$Close = as.numeric(cu$Close)
cu = na.omit(cu)
colnames(cu)[2] = "copper"
colnames(cu)

# clean gold data
au = read.csv("Gold.csv")
au$Date = as.Date(au$Date)
colnames(au)[2] = "gold"
au = au[year(au$Date) >= 2015,c("Date", "gold")]
au$gold = as.numeric(au$gold)
au = na.omit(au)

# clean silver data
ag = read.csv("Silver.csv")
ag$Date = as.Date(ag$Date)
colnames(ag)[2] = "silver"
ag = ag[year(ag$Date) >= 2015,c("Date", "silver")]
ag$silver = as.numeric(ag$silver)
ag = na.omit(ag)

# clean crude oil data
oil = read.csv("Crude_Oil.csv")
oil$Date = as.Date(oil$Date)
oil = oil[year(oil$Date) >= 2015,c("Date", "Close")]
colnames(oil)[2] = "crude_oil"
oil$crude_oil = as.numeric(oil$crude_oil)
oil = na.omit(oil)

# join all commodities
commodity = Reduce(function(df1, df2) inner_join(df1, df2, by="Date"), list(al, cu, au, ag, oil))

setwd("D:/PycharmProjects/GU-ANLY-501-FALL-2021/data")
write.csv(commodity, "commodity.csv", row.names = FALSE)
