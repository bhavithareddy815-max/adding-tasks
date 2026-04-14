from db_config import get_db_connection

def create_user(name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (name, email)
    )
    conn.commit()
    user_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return user_id

def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email FROM users")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user