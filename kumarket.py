import requests
import pandas as pd

# GET all market-pairs on Kucoin via /api/v1/symbols

# KUCOIN API
api_url = "https://api.kucoin.com"
csv_name = "Kucoin_Market-Pairs"

# API CALL
data = requests.get(f"{api_url}/api/v1/symbols",
	headers = {"content-type":"application/json"})
    
# CSV EXPORT   
df = pd.DataFrame(data.json()["data"],
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

# df = df[["symbol","name","market"]]
df.sort_values(by='symbol', inplace=True)
df.to_csv(csv_name+'.csv', header=True, index=False)