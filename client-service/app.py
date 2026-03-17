from flask import Flask, jsonify
import requests

app=Flask(__name__)

@app.route("/external-users")
def get_esternal_users():
    response = requests.get("http://users-service:5001/users")
    return jsonify(response.json())

app.run(host="0.0.0.0", port=5002)