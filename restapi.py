import flask
from flask import jsonify
from flask import request
from TWsql import create_con
from TWsql import execute_read_query
import Creds

#setting up an application name
app = flask.Flask(__name__) #sets up the app
app.config["DEBUG"] = True #allow to show errors in browser

cars = [
    {'id': 0,
    "make": "Jeep",
    "model": "Grand Cherokee",
    "year": "2000",
    "color": "black"
    },
    {'id': 1,
    "make": "Ford",
    "model": "mustang",
    "year": "1970",
    "color": "white"
    },
    {'id': 2,
    "make": "Dodge",
    "model": "challenger",
    "year": "2020",
    "color": "red"
    }
]



@app.route('/', methods=["GET"]) #default url without any routing as GET
def home():
    return "<H1>WELCOME TO OUR FIRST API</H1>"

@app.route('/api/car/all', methods=["GET"]) #ENDPOINT TO GET ALL CARS
def all_calls():
    return jsonify(cars)

@app.route('/api/car', methods=["GET"]) #get a single car by id: http://127.0.0.1:5000/api/car?id=1
def api_id():
    if "id" in request.args:
        id = int(request.args['id'])
    else: return "Error: No id provided"
    results = []
    for car in cars:
        if car["id"] == id:
            results.append(car)
    return jsonify(results)

@app.route('/api/car', methods=['POST']) #ADD A CAR
def add_car():
    request_data = request.get_json()
    new_id = request_data['id']
    newmake = request_data['make']
    newmodel = request_data['model']
    newyear = request_data['year']
    newcolor = request_data['color']

    cars.append({'id': new_id, "make": newmake, "model": newmodel, "year": newyear, "color": newcolor})
    return "add request successful"

@app.route('/api/car', methods=["DELETE"])
def delete_ex():
    request_data = request.get_json()
    infodelete = request_data['id']
    for i in range(len(cars) -1, -1, -1):
        if cars[i]['id'] == infodelete:
            del[cars[i]]
    return "delete request successful"

@app.route('/api/users', methods=['GET']) #api to get a user from the db table in aws
def api_users_id():
    if 'id' in request.args: #only if an id is provided
        id = int(request.args['id'])
    else:
        return "Error: no ID prvided"
    
    myCreds = Creds.Creds()
    conn = create_con(myCreds.conString, myCreds.userName, myCreds.password, myCreds.databaseName)
    sql = "Select * from users"
    users = execute_read_query(conn, sql)
    results = []

    for user in users:
        if user['id'] == id:
            results.append(user)
    return jsonify(results)


app.run()