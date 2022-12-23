from flask import Flask, jsonify, abort, request
from stocksDAO import stocksDAO

app = Flask(__name__, static_url_path='', static_folder='static')

# # stocks = [
#     {'name':'stock1'},
#     {'name':'stock2'},
#     {'name':'stock3'},
#     ]

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


#curl "http://127.0.0.1:5000/books/2"
@app.route('/stocks/<int:id>', methods=['GET'])
def findById(id):
    findstocks = stocksDAO.findByID(id)

    return jsonify(findstocks)

# @app.route('/vote/<bandname>', methods=['GET'])
# def getCountForBand(bandname):
#     count = voteDAO.countvotes(bandname)
#     return jsonify({bandname:count})

# @app.route('/vote', methods=['GET'])
# def getAllCount():
#     allcounts = []
#     for band in bands:
#         bandname = band['name'] 
#         count = voteDAO.countvotes(bandname)
#         allcounts.append({bandname:count})
#     return jsonify(allcounts)

# @app.route('/vote/all', methods=['delete'])
# def deleteAllVote():
#     return jsonify({'done':True})



#curl  -i -H "Content-Type:application/json" -X POST -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books
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


#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
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