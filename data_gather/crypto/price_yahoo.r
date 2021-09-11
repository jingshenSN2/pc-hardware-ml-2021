library(httr)

setwd("D:/PycharmProjects/GU-ANLY-501-FALL-2021/data_gather/crypto/yahoo_finance")

today = "2021-09-10"

get_crypto_price = function(crypto) {
    print(paste("Downloading historical price of", crypto))
    ts = as.numeric(as.POSIXct(today, format="%Y-%m-%d"))
    url = paste0("https://query1.finance.yahoo.com/v7/finance/download/", crypto, "-USD?")
    q = list("period1"=0, "period2"=ts, "interval"="1d", "events"="history", "includeAdjustedClose"=TRUE)
    rep = httr::GET(url, add_headers("User-Agent"="Mozilla/5.0"), query=q)
    save = paste0(crypto, "-USD.csv")
    df = httr::content(rep)
    write.csv(df, save, row.names=FALSE)
}

get_crypto_price("BTC")
get_crypto_price("ETH")
get_crypto_price("DOGE")
get_crypto_price("BCH")
get_crypto_price("LTC")
get_crypto_price("ETC")
get_crypto_price("XMR")
get_crypto_price("DASH")
get_crypto_price("XCH")
