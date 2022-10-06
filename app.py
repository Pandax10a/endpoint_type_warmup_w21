# modules to make this work, flask for api end point, dbhelpers for connection, json for data in json
from flask import Flask, request
import dbhelpers as dh
import json

app = Flask(__name__)



# needs 3 argument(name, description, quantity) to add new item to db and returns the item's id as json
@app.post('/api/restaurant')

def add_new_restaurant():
    
    restaurant_name = request.json.get('name')
    restaurant_address = request.json.get('address')
    restaurant_phone = request.json.get('phone')
    restaurant_img = request.json.get('img_url')
    

    result = dh.run_statement('CALL add_new_restaurant(?, ?, ?, ?)', [restaurant_name, restaurant_address, restaurant_phone, restaurant_img] )

    if(type(result) == list):
        restaurant_json = json.dumps(result, default=str)
        return restaurant_json
    else:
        print('error, error, error ')



app.run(debug=True)