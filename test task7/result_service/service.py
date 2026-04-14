from db.connection import get_connection
from exceptions import ResultCalculationException


def get_result(student_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT AVG(marks) as average FROM marks WHERE student_id=%s",
        (student_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if result["average"] is None:
        raise ResultCalculationException("No marks available")

    return result