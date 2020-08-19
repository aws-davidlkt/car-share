from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def healthCheckResponse():
    return jsonify({"message" : "health check OK!. Try /get-cars instead."})
    

@app.route('/get-cars')
def get_cars():
    response = Response(open("cars-list.json").read())
    response.headers["Content-Type"]= "application/json"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')