from db.connection import get_connection
from exceptions import StudentNotFoundException


def add_student(id, name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (id, name) VALUES (%s, %s)",
        (id, name)
    )

    conn.commit()
    conn.close()

    return {"message": "Student added successfully"}


def get_students():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    return students


def get_student(student_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM students WHERE id=%s",
        (student_id,)
    )

    student = cursor.fetchone()

    conn.close()

    if not student:
        raise StudentNotFoundException("Student not found")

    return student