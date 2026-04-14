from db_config import get_db_connection

def create_order(user_id, product, quantity):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (user_id, product, quantity) VALUES (%s, %s, %s)",
        (user_id, product, quantity)
    )
    conn.commit()
    order_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return order_id

def get_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, user_id, product, quantity FROM orders")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data