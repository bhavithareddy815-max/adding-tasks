from flask import Flask, request, jsonify
import requests
from repository.order_repository import create_order, get_orders

app = Flask(__name__)
USER_SERVICE_URL = "http://localhost:5001"

def validate_user(user_id: int) -> bool:
    r = requests.get(f"{USER_SERVICE_URL}/users/{user_id}", timeout=2)
    return r.status_code == 200

@app.post("/orders")
def add_order():
    data = request.json or {}
    user_id = data.get("user_id")
    product = data.get("product")
    quantity = data.get("quantity")

    if user_id is None or not product or quantity is None:
        return jsonify({"error": "user_id, product, quantity are required"}), 400

    try:
        user_id = int(user_id)
        quantity = int(quantity)
        if quantity <= 0:
            return jsonify({"error": "quantity must be > 0"}), 400
    except ValueError:
        return jsonify({"error": "user_id and quantity must be numbers"}), 400

    # Service-to-service communication (Order -> User)
    try:
        if not validate_user(user_id):
            return jsonify({"error": "Invalid user_id (user not found)"}), 400
    except requests.RequestException:
        return jsonify({"error": "User service unavailable"}), 503

    order_id = create_order(user_id, product, quantity)
    return jsonify({"message": "Order created", "order_id": order_id}), 201

@app.get("/orders")
def orders():
    return jsonify(get_orders()), 200

if __name__ == "__main__":
    app.run(port=5002, debug=True)