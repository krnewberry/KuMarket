import requests
import pandas as pd

# KUCOIN API
api_url = "https://api.kucoin.com"
csv_name = "Kucoin_Market-Pairs"

# API CALL
KuMarketData = requests.get(f"{api_url}/api/v1/symbols",
	headers = {"content-type":"application/json"})

# DATA FRAME 
df = pd.DataFrame(KuMarketData.json()["data"],
    columns = ['symbol',
    'name',
    'baseCurrency',
    'quoteCurrency',
    'market',
    'baseMinSize',
    'quoteMinSize',
    'baseMaxSize',
    'quoteMaxSize',
    'baseIncrement',
    'quoteIncrement',
    'priceIncrement',
    'feeCurrency',
    'enableTrading',
    'isMarginEnabled',
    'priceLimitRate'])

# CSV - INCLUDE THESE COLUMNS ONLY:
df = df[["symbol", "quoteCurrency", "market"]]

# CSV - EXPORT
df.sort_values(by='quoteCurrency', inplace=True)
df.to_csv(csv_name+'.csv', header=True, index=False)

print("Success...")