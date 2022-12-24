import requests



def stockhistory(ticker):
    url = "https://mboum-finance.p.rapidapi.com/hi/history"

    querystring = {"symbol":ticker,"interval":"15m","diffandsplits":"false"}

    headers = {
	    "X-RapidAPI-Key": "cb13e099f6msh76bac0554262195p1e57e4jsnec3cb7675f2c",
	    "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

ticker = input("Input your stock ticker: \n")

stockhistory(ticker)