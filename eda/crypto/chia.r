library(ggplot2)
library(ggthemes)
# devtools::install_github('cttobin/ggthemr')
library(ggthemr)
ggthemr('fresh')
Sys.setlocale("LC_TIME", "English")
setwd("D:/PycharmProjects/GU-ANLY-501-FALL-2021/data")

chia = read.csv("chia.csv")
chia$Date = as.Date(chia$Date)
p = ggplot(data=chia, aes(x=Date, y=chia.price))
p + geom_line() +
  theme_calc() +
  labs(x = "Year 2021", y = 'Price(USD)', title = "Historical Price of Chia Network")
  
ggsave("../eda/crypto/chia_price.png")

p = ggplot(data=chia, aes(x=Date, y=market.cap))
p + geom_line() +
  theme_calc() +
  labs(x = "Year 2021", y = 'Market Capacity(USD)', title = "Historical Market Capacity of Chia Network")

ggsave("../eda/crypto/chia_makcap.png")

chia$netspace = chia$netspace / 1024**6

p = ggplot(data=chia, aes(x=Date, y=netspace))
p + geom_line() +
  theme_calc() +
  labs(x = "Year 2021", y = 'Net Space(Exabyte, EiB)', title = "Historical Net Space of Chia Network")

ggsave("../eda/crypto/chia_netspace.png")
