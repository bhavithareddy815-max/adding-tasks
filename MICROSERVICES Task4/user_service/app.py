from flask import Flask, request, jsonify
import mysql.connector
from repository.user_repository import create_user, get_users, get_user_by_id

app = Flask(__name__)

@app.post("/users")
def add_user():
    data = request.json or {}
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    try:
        user_id = create_user(name, email)
        return jsonify({"message": "User created", "user_id": user_id}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409
    except Exception:
        return jsonify({"error": "User service error"}), 500

@app.get("/users")
def users():
    return jsonify(get_users()), 200

@app.get("/users/<int:user_id>")
def user_by_id(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

if __name__ == "__main__":
    app.run(port=5001, debug=True)