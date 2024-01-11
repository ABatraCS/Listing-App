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

# clientCursor.execute("INSERT INTO available_listings (userID, beds, baths, rent, term) VALUES (1, 4, 4, 1000, 'Fall')")
# db.commit()
clientCursor.execute("SELECT * FROM available_listings")

for x in clientCursor:
    print(x)