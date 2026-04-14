from db_config import get_db_connection

def save_feedback(name, email, message):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO feedback (name, email, message)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (name, email, message))
    conn.commit()

    cursor.close()
    conn.close()