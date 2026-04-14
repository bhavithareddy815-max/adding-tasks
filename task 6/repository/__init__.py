from db_config import get_db_connection

def get_daily_activity_report():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT DATE(changed_at) AS log_date,
               COUNT(*) AS total_changes
        FROM employee_log
        GROUP BY DATE(changed_at)
        ORDER BY log_date DESC
    """)

    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def get_detailed_logs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM employee_log
        ORDER BY changed_at DESC
    """)

    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result