library(httr)

setwd("D:/PycharmProjects/GU-ANLY-501-FALL-2021/data_gather/commodity/data")

get_commodity_price = function(code, filename) {
    print(paste("Downloading historical price of", code))
    ts = as.numeric(as.POSIXct(Sys.Date(), format="%Y-%m-%d"))
    url = paste0("https://query1.finance.yahoo.com/v7/finance/download/", code, "?")
    q = list("period1"=0, "period2"=ts, "interval"="1d", "events"="history", "includeAdjustedClose"=TRUE)
    rep = httr::GET(url, add_headers("User-Agent"="Mozilla/5.0"), query=q)
    save = paste0(filename, ".csv")
    df = httr::content(rep)
    write.csv(df, save, row.names=FALSE)
}

get_commodity_price("HG=F", "Copper")
get_commodity_price("ALI=F", "Aluminum")
get_commodity_price("CL=F", "Crude_Oil")
