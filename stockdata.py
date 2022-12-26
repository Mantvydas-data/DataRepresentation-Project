import requests



def stockhistory(ticker):
    url = "https://mboum-finance.p.rapidapi.com/hi/history"

    querystring = {"symbol":ticker,"interval":"15m","diffandsplits":"false"}

    headers = {
	    "X-RapidAPI-Key": "apikey",
	    "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

ticker = input("Input your stock ticker: \n")

stockhistory(ticker)
