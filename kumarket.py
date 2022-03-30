import requests
import pandas as pd
import time
from datetime import datetime, timezone

# GET MARKET PAIRINGS FROM KUCOIN /api/v1/symbols

# KUCOIN API
api_url = "https://api.kucoin.com"
api_rate_limit = 1
csv_name = "Kucoin_Market-Pairs"

# API CALL
data = requests.get(f"{api_url}/api/v1/symbols",
	headers = {"content-type":"application/json"})
    
# CSV EXPORT   
df = pd.DataFrame(data.json()["data"],
    columns = ["symbol","name","baseCurrency","quoteCurrency","market","baseMinSize","quoteMinSize","baseMaxSize","quoteMaxSize","baseIncrement","quoteIncrement","priceIncrement","feeCurrency","enableTrading","isMarginEnabled","priceLimitRate"])
df = df[["symbol","name","market","enableTrading"]]
df.sort_values(by='symbol', inplace=True)
df.to_csv(csv_name+'.csv', mode='a', header=True, index=False)
