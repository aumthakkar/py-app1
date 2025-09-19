
from flask import Flask, jsonify
import time
import socket

app = Flask(__name__)

@app.route('/api/v1/info')
# ‘/’ URL is bound with hello_world() function.
def info():
    return jsonify({
        "time" : time.ctime(),
        "hostname" : socket.gethostname(),
        "message" : "Hi, Pranav! You are doing great, Pranav!"
    })

@app.route('/api/v1/healthz')
# ‘/’ URL is bound with hello_world() function.
def health():
    return jsonify({
        "status" : "up"
    })

# main driver function
if __name__ == '__main__':

    app.run(host = "0.0.0.0")