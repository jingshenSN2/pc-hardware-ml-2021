# install api package
# install.packages("Quandl")

# import library and set api_key
my_api_key = "8n7Kv1Q46yvHbp9z9k23"
library(Quandl)
Quandl.api_key(my_api_key)

setwd("D:/PycharmProjects/GU-ANLY-501-FALL-2021/data_gather/commodity/data")

save_metal = function(Quandl_code, filename) {
  start_date = "2014-01-01"
  end_date = Sys.Date()
  metal = Quandl(Quandl_code, type="raw", collapse="daily", start_date=start_date, end_date=end_date)
  metalFile = file(paste0(filename, ".csv"))
  write.csv(metal, metalFile, row.names=FALSE)
}

save_metal("LBMA/GOLD", "Gold")
save_metal("LBMA/SILVER", "Silver")
