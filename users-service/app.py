from flask import Flask, request, jsonify

app=Flask(__name__)

users = {
    1: {"name": "Alex"},
    2: {"name": "Maria"}
}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    return jsonify(users.get(id, {}))

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    new_id = len(users) + 1
    users[new_id] = data
    return jsonify({"created": new_id}), 201

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    users[id] = request.json
    return jsonify({"updated": id})

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    users.pop(id, None)
    return jsonify({"deleted": id})

app.run(host="0.0.0.0", port=5001)
