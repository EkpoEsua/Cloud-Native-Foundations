from flask import Flask
from flask import json
import logging


app = Flask(__name__)

@app.route("/")
def hello():

    #implement the logging functionality using Flask's inbuilt logger
    app.logger.info('root endpoint was reached')

    #implement the logger using python's default loggger
    # logging.info("root endpoint was reached")

    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response = json.dumps({'result':'OK - Healthy'}),
        status = 200,
        mimetype = 'application/json'
    )
    
    #implement the logging functionality using Flask's inbuilt logger
    app.logger.info('status endpoint was reached')

    #implement the logger using python's default loggger
    # logging.info("status endpoint was reached")

    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response = json.dumps(
            {
                "status":"sucess",
                "code":0,
                "data":{
                    "UserCount":140,
                    "UserCountActive":23
                }
            }
        ),
        status = 200,
        mimetype = "application/json"
    )
    
    #implement the logging functionality using Flask's inbuilt logger
    app.logger.info('metrics endpoint was reached')

    #implement the logger using python's default loggger
    # logging.info("metrics endpoint was reached")

    return response

if __name__ == "__main__":
    logging.basicConfig(
        filename='app.log',
        level=logging.DEBUG,
        style='{',
        format='{asctime} , {message}'
    )

    app.run(host='0.0.0.0')
