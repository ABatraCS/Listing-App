import mysql.connector
from flask import Flask, jsonify, request
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

#Create a new listing
@app.route('/listings', methods = ['POST'])
def create_listing():
    new_listing = request.get_json()

    #Fields to pass
    user = new_listing.get('userID')
    num_beds = new_listing.get('beds')
    num_baths = new_listing.get('baths')
    rent_amt = new_listing.get('rent')
    housing_term = new_listing.get('term')
    insert_query = "INSERT INTO available_listings (userID, beds, baths, rent, term) VALUES (%d, %d, %d, %d, %s)"

    clientCursor.execute(insert_query, (user, num_beds, num_baths, rent_amt, housing_term))
    db.commit

    return jsonify({'message': 'Listing created successfully'}), 201

#Get listing by listingID
@app.route('/listings<int:id>', methods = ['GET'])
def get_listing(id):
    #Find corresponding json
    get_query = "SELECT * from available_listings WHERE listingID = %d"
    clientCursor.execute(get_query, (id))
    row = clientCursor.fetchone()
    result = {}

    for i, col in enumerate(clientCursor.description):
        result[col[0]] = row[i]

    return jsonify(result)
    
#Update a listing
@app.route('/listings<int:id>', methods = ['PUT'])
def update_listing(id):
    updated_listing = request.get_json()
    num_beds = updated_listing.get('beds')
    num_baths = updated_listing.get('baths')
    rent_amt = updated_listing.get('rent')
    housing_term = updated_listing.get('term')
    update_query = "UPDATE available_listings SET beds = %d, baths = %d, rent = %d, term = %s"

    clientCursor.execute(update_query, (num_beds, num_baths, rent_amt, housing_term))
    db.commit()

    return jsonify({'message': 'Listing updated successfully'})

#Delete a listing
@app.route('/listings<int:id>', methods = ['DELETE'])
def delete_listing(id):
    delete_query = "DELETE FROM available_listings WHERE listingID = %d"
    clientCursor.execute(delete_query, (id))
    db.commit()

    return jsonify({'message' : 'Listing deleted successfully'})

if __name__ == '__main__':
    app.run(debug = True)


