from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS
import carShareTableClient

app = Flask(__name__)
CORS(app)

@app.route('/')
def healthCheckResponse():
    return jsonify({"message" : "We made it just fine!. Try /cars instead."})
    

# @app.route('/get-cars')
# def get_cars():
#     response = Response(open("cars-list.json").read())
#     response.headers["Content-Type"]= "application/json"
#     return response

#Retrieve all cars or provide querystring params
@app.route("/cars", methods=['GET'])
def getCars():

    filterCategory = request.args.get('filter')
    if filterCategory:
        filterValue = request.args.get('value')
        queryParam = {
            'filter': filterCategory,
            'value': filterValue
        }
        serviceResponse = carShareTableClient.queryCars(queryParam)
    else:
        serviceResponse = carShareTableClient.getAllCars()

    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

#Retrieve a specific car by providing path parameter ID
@app.route("/cars/<Id>", methods=['GET'])
def getcar(Id):
    serviceResponse = carShareTableClient.getCar(Id)

    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

# increment the number of likes for the provided car.
@app.route("/cars/<Id>/like", methods=['POST'])
def likeCar(Id):
    serviceResponse = carShareTableClient.likeCar(Id)

    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

# indicate that the provided car should be marked as reserved.
@app.route("/cars/<Id>/reserve", methods=['POST'])
def reserveCar(Id):
    serviceResponse = carShareTableClient.reserveCar(Id)

    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse

if __name__ == '__main__':
    app.run(host='0.0.0.0')