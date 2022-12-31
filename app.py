from flask import Flask, jsonify, abort, request, render_template
from stocks_db import StocksDAO
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import os

# Load environment variables to import keys and parameters from .env
load_dotenv()

app = Flask(__name__, static_url_path='', template_folder="templates")
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config['MYSQL_HOST'] = os.environ["MYSQL_HOST"]
app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = os.environ["MYSQL_DB"]

# https://stackoverflow.com/a/46637194/19501420
# For some reason without this requests do not work.
CORS(app)

# Calling StockDAO class and creating initial datbase with a table
StocksDAO = StocksDAO()
StocksDAO.createdatabase()
StocksDAO.createtable()
data = ("NVDA", "NVIDIA", "390.45", "5.213")
StocksDAO.create(data)

# To get all stocks
@app.route('/stocks', methods=['GET'])
def getAll():
    result=StocksDAO.getAll()
    response = jsonify(result)
    return response

# To call to third party API returning stock market data
@app.route('/mboum/<tickername>', methods=['GET'])
def mboum(tickername):
    if tickername:

        querystring = {"symbol":tickername,"interval":"1d","diffandsplits":"false"}
        url = os.environ["MBOUMFINANCE_API_HOST"]

        headers = {
            "X-RapidAPI-Key": os.environ["MBOUMFINANCE_API_KEY"],
            "X-RapidAPI-Host": os.environ["THIRD_API_HOST"]
        }
        response = requests.get(url, headers=headers, params=querystring)
        return jsonify(response.json())
    else:
        abort(400)

# To get stock by id
@app.route('/stocks/<int:id>', methods=['GET'])
def findById(id):
    findstocks = StocksDAO.findByID(id)
    return jsonify(findstocks)

# To redirect to main page
@app.route('/')
def portfolio():
    return render_template("portfolio.html")

# To redirect to stock comparison page
@app.route('/compare', methods=['GET'])
def compare():
    return render_template("compare.html")

# To create a new stock
@app.route('/stocks', methods=['POST'])
def create():
    
    data = request.get_json()
    
    stock = {
        "ticker": data['ticker'],
        "sname": data['sname'],
        "pprice": data['pprice'],
        "quantity": data['quantity'],
    }
    values =(stock['ticker'],stock['sname'],stock['pprice'],stock['quantity'])
    newId = StocksDAO.create(values)
    stock['id'] = newId
    return jsonify(stock)


# To find sock by id and update it
@app.route('/stocks/<int:id>', methods=['PUT'])
def update(id):
    foundstock = StocksDAO.findByID(id)
    if not foundstock:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'pprice' in reqJson and type(reqJson['pprice']) is not float:
        abort(400)

    if 'ticker' in reqJson:
        foundstock['ticker'] = reqJson['ticker']
    if 's' in reqJson:
        foundstock['sname'] = reqJson['sname']
    if 'pprice' in reqJson:
        foundstock['pprice'] = reqJson['pprice']
    if 'quantity' in reqJson:
        foundstock['quantity'] = reqJson['quantity']
    values = (foundstock['ticker'],foundstock['sname'],foundstock['pprice'],foundstock['quantity'],foundstock['id'])
    StocksDAO.update(values)
    return jsonify(foundstock)
        

# To find sock by id and delete it
@app.route('/stocks/<int:id>' , methods=['DELETE'])
def delete(id):
    StocksDAO.delete(id)
    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=os.environ["FLASK_DEBUG"])