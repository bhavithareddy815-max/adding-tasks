from db.connection import get_connection
from exceptions import MarksNotFoundException


def add_marks(student_id, subject, marks):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO marks (student_id, subject, marks) VALUES (%s,%s,%s)",
        (student_id, subject, marks)
    )

    conn.commit()
    conn.close()

    return {"message": "Marks added successfully"}


def get_marks(student_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT subject, marks FROM marks WHERE student_id=%s",
        (student_id,)
    )

    marks = cursor.fetchall()

    conn.close()

    if not marks:
        raise MarksNotFoundException("Marks not found")

    return marks