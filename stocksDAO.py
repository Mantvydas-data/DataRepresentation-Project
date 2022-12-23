import mysql.connector
import dbconfig as cfg
class StocksDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']
        self.auth_plugin= cfg.mysql['auth_plugin']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
            auth_plugin= self.auth_plugin,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def create(self, values):
        cursor = self.getcursor()
        sql="insert into stocks (ticker, name, pprice, quantity) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getcursor()
        sql="select * from db.stocks"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from db.stocks where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, values):
        cursor = self.getcursor()
        sql="update stocks set ticker= %s, name=%s, pprice=%s, quantity=%s, where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from stocks where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id', 'ticker', 'name', "pprice", "quantity"]
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item

    def createtable(self):
        cursor = self.getcursor()
        sql="create table stocks (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, ticker varchar(8), name varchar(250), pprice float(4,2), quantity float(10,2))"
        cursor.execute(sql)

        self.connection.commit()
        self.closeAll()

    def createdatabase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
        self.cursor = self.connection.cursor()
        sql="create database "+ self.database
        self.cursor.execute(sql)

        self.connection.commit()
        self.closeAll()
        
stocksDAO = StocksDAO()

if __name__ == "__main__":
#     #stocksDAO.createdatabase()
#     #stocksDAO.createtable()

    # data = ("NVDA", "NVIDIA", "390.45", "5.213")
    # stocksDAO.create(data)
#     # count = voteDAO.countvotes('climbing club')
#     # print (count)

    print("sanity")