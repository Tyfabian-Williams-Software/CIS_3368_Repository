import hashlib
import datetime
import time
import flask
from flask import jsonify
from flask import request, make_response

app = flask.Flask(__name__) #sets up the app
app.config["DEBUG"] = True #allow to show errors in browser

masterPassword = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
masterUsername = "username"
validTokens = {"100", "200", '300', '400'}



#basic browser http auth, prompts username and password
#"password" as plaintext shoeld not be allowed
#we shoould hash it and compare it to the hash

@app.route("/authentificatedroute", methods=['GET'])
def auth_example():
    if request.authorization:
        encoded = request.authorization.password.encode() #unicode encoding
        hashedResult = hashlib.sha256(encoded) #hashing
        if request.authorization.username == masterUsername and hashedResult.hexdigest() == masterPassword:
            return '<h1> You are allowed to be here </h1>'
    return make_response('Could not Verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})

#toekn submission as part of the url, similar to how personal SMS / text codes are used
@app.route('/api/token/<token>', methods=['GET'])
def auth_token(token):
    for validtoken in validTokens:
        if token == validtoken:
            return '<h1> Congrats, Auth was successful! </h1>'
    return "Invalid Access Token"

#create token submissions that have an expiration date
#valid til Jan 1, 2030: 1893456000
#valid til Jan 1, 2022: 1640995200

#we can create these tokens:
# date  = datetime.datetime.(2022, 1, 1)
# dateinSeconds = date.timestamp() #time in seconds

@app.route('/api/timetoken/<timetoken>', methods=['GET'])
def auth_timetoken(timetoken):
    if float(timetoken) > time.time():
        return "<h1> SUCCESS </H1>"
    return "Token expired"

app.run()