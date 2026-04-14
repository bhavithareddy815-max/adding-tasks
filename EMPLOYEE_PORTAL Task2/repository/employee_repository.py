from db_config import get_db_connection


def create_employee(employee_id, name, email, password, department):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO employees
            (employee_id, name, email, password, department)
            VALUES (%s, %s, %s, %s, %s)
        """, (employee_id, name, email, password, department))

        conn.commit()
        return True

    except:
        return False

    finally:
        cursor.close()
        conn.close()


def get_employee_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees WHERE email = %s", (email,))
    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    return employee