import flask
from flask import jsonify
from flask import request
from TWsql import create_con
from TWsql import execute_read_query
from TWsql import execute_query
import Creds

#setting up an application name
app = flask.Flask(__name__) #sets up the app
app.config["DEBUG"] = True #allow to show errors in browser


#This sets up a call to the AWS db and uses get to display all entries in JSON
@app.route('/api/inventory/all', methods=['GET'])
def inv_all():
    myCreds = Creds.Creds()
    conn = create_con(myCreds.conString, myCreds.userName, myCreds.password, myCreds.databaseName)
    sql = "SELECT * FROM tires"
    tires = execute_read_query(conn, sql)
    results = []

    for tire in tires:
        results.append(tire)
    return jsonify(results)

@app.route('/api/inventory/add', methods=['POST'])
def add_tire():
    request_data = request.get_json()
    newbrand = request_data.get('brand')
    newmodel = request_data.get('model')
    newloadrating = request_data.get('loadrating')
    newspeedrating = request_data.get('speedrating')
    newtype = request_data.get('type')
    newstock = request_data.get('stock')

    myCreds = Creds.Creds()
    conn = create_con(myCreds.conString, myCreds.userName, myCreds.password, myCreds.databaseName)
    sql = "INSERT INTO tires (brand, model, loadrating, speedrating, type, stock) VALUES ('%s', '%s', '%s', '%s', '%s', %s);" % (newbrand, newmodel,newloadrating, newspeedrating, newtype, newstock)
    execute_query(conn, sql)
    
    return "Success"

@app.route('/api/inventory/delete', methods=['DELETE'])
def tire_delete():
    request_data = request.get_json()
    idToDelete = request_data.get('id')

    myCreds = Creds.Creds()
    conn = create_con(myCreds.conString, myCreds.userName, myCreds.password, myCreds.databaseName)
    sql = "Delete from tires where id = %s;" % (idToDelete)
    execute_query(conn, sql)
    return "Deleted"
    
@app.route('/api/inventory/update', methods=['PUT'])
def tire_stock_update():
    request_data = request.get_json()
    IdToUpdate = request_data.get('id')
    stockUpdate = request_data.get('stock')

    myCreds = Creds.Creds()
    conn = create_con(myCreds.conString, myCreds.userName, myCreds.password, myCreds.databaseName)
    sql = "UPDATE tires SET stock= %s where id = %s;" % (stockUpdate,IdToUpdate)
    execute_query(conn, sql)
    return "Stock updated"


app.run()