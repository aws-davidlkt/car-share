from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS
import carShareTableClient

app = Flask(__name__)
CORS(app)

@app.route('/')
def healthCheckResponse():
    return jsonify({"message" : "u reached it OK!. Try /cars instead."})
    

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
@app.route("/cars/<id>", methods=['GET'])
def getcar(id):
    serviceResponse = carShareTableClient.getCar(id)

    flaskResponse = Response(serviceResponse)
    flaskResponse.headers["Content-Type"] = "application/json"

    return flaskResponse


if __name__ == '__main__':
    app.run(host='0.0.0.0')