from db_config import get_db_connection

def insert_student(name, email, dob, department, phone):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students (name, email, dob, department, phone)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, dob, department, phone))

    conn.commit()
    cursor.close()
    conn.close()

def get_all_students():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT id, name, email, dob, department, phone FROM students ORDER BY id DESC"
    cursor.execute(query)
    rows = cursor.fetchall()

    cursor.close()
    conn.close()
    return rows
