from flask import Flask, json
import logging

app = Flask(__name__)

@app.route("/status", methods=['GET'])
def health_status():
    data = {"result": "OK - healthy"}
    response = app.response_class(
        response = json.dumps(data),
        status = 200,
        mimetype = "application/json"
    )
    app.logger.info('status endpoint was reached')
    return response

@app.route("/metrics", methods=['GET'])
def show_metrics():
    data = {"UserCount": 140, "UserCountActive": 23}
    response = app.response_class(
        response = json.dumps({"status": "success", "code": 0, "data": data}),
        status = 200,
        mimetype = "application/json"
    )
    app.logger.info('metrics endpoint was reached')
    return response

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s, %(message)s')
    app.run(debug=True, host='0.0.0.0')
