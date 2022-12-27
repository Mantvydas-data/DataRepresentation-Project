import requests
import json
import pandas as pd
import matplotlib.pyplot as plt    
from dbconfig import apikey as keys

apikey = keys['key'] 

def stockhistory(ticker):
    url = "https://mboum-finance.p.rapidapi.com/hi/history"

    querystring = {"symbol":ticker,"interval":"1d","diffandsplits":"false"}

    headers = {
	    "X-RapidAPI-Key": apikey,
	    "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    x=response.json()

    df2 = pd.DataFrame.from_dict(x['items'], orient="index")
    df3 = df2[['date','close']]
    
    df3.set_index('date', inplace=True)
    print(df3)
    df3.plot()
    df = pd.Series(data=df3['close'])
    plt.title("Stock Price Graph")
    plt.xlabel("Date")
    plt.ylabel("Stock price")
    plt.show()



ticker = input("Input your stock ticker: \n")

#getAllAsFile(ticker)
stockhistory(ticker)



# https://bobbyhadz.com/blog/python-typeerror-the-json-object-must-be-str-bytes-or-bytearray-not-response#:~:text=The%20Python%20%22TypeError%3A%20the%20JSON,json()%20.
# https://sparkbyexamples.com/pandas/pandas-convert-json-to-dataframe/