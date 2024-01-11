import mysql.connector
from flask import Flask
import json

#Establish connection with "listings" db
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "listings"
)

clientCursor = db.cursor()
app = Flask(__name__)

#Create

#Read
@app.route('/available_listings/<int:id>/get')
def getListing(id):
    clientCursor.execute("SELECT * from available_listings WHERE listingID = %d" % id)
    row = clientCursor.fetchone()
    result = []
    d = {}

    for i, col in enumerate(clientCursor.description):
        d[col[0]] = row[i]

    result.append(d)

    return json.dumps(result)
    
#Update
    
#Delete

if __name__ == '__main__':
    app.run(debug = True)


