from flask import Flask, jsonify, abort, request
from stocksDAO import stocksDAO

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/stocks')
def getAll():
    result=stocksDAO.getAll()
    return jsonify(result)

# @app.route('/add/<stockname>', methods=['POST'])
# def addNewStock(stockname):
#     ip_addr = request.remote_addr
#     data = (stockname, ip_addr)
#     #newid = voteDAO.create(data)

#     return jsonify({'id':newid})


@app.route('/stocks/<int:id>', methods=['GET'])
def findById(id):
    findstocks = stocksDAO.findByID(id)

    return jsonify(findstocks)


@app.route('/stocks', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    stock = {
        "ticker": request.json['ticker'],
        "name": request.json['name'],
        "pprice": request.json['pprice'],
        "quantity": request.json['quantity'],
    }
    values =(stock['ticker'],stock['name'],stock['pprice'],stock['quantity'])
    newId = stocksDAO.create(values)
    stock['id'] = newId
    return jsonify(stock)


@app.route('/stocks/<int:id>', methods=['PUT'])
def update(id):
    foundstock = stocksDAO.findByID(id)
    if not foundstock:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'pprice' in reqJson and type(reqJson['pprice']) is not int:
        abort(400)

    if 'Ticker' in reqJson:
        foundstock['ticker'] = reqJson['ticker']
    if 'name' in reqJson:
        foundstock['name'] = reqJson['name']
    if 'pprice' in reqJson:
        foundstock['pprice'] = reqJson['pprice']
    if 'quantity' in reqJson:
        foundstock['quantity'] = reqJson['quantity']
    values = (foundstock['ticker'],foundstock['name'],foundstock['pprice'],foundstock['quantity'],foundstock['id'])
    stocksDAO.update(values)
    return jsonify(foundstock)
        


@app.route('/stocks/<int:id>' , methods=['DELETE'])
def delete(id):
    stocksDAO.delete(id)
    return jsonify({"done":True})



if __name__ == "__main__":
    app.run(debug=True)