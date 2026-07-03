import sqlite3


def get_dashboard_data():

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    # Total Users
    cursor.execute("SELECT COUNT(*) FROM users")
    total_users = cursor.fetchone()[0]

    # Voice Logins
    cursor.execute("""
        SELECT COUNT(*)
        FROM login_history
        WHERE method='Voice'
          AND status='Success'
    """)
    voice_logins = cursor.fetchone()[0]

    # Face Logins
    cursor.execute("""
        SELECT COUNT(*)
        FROM login_history
        WHERE method='Face'
          AND status='Success'
    """)
    face_logins = cursor.fetchone()[0]

    # Total Successful Logins
    cursor.execute("""
        SELECT COUNT(*)
        FROM login_history
        WHERE status='Success'
    """)
    total_logins = cursor.fetchone()[0]

    # Login History (only existing users)
    cursor.execute("""
    SELECT
        username,
        method,
        status,
        login_time
    FROM login_history
    ORDER BY login_time DESC
""")

    history = cursor.fetchall()

    conn.close()

    return {
        "total_users": total_users,
        "voice_logins": voice_logins,
        "face_logins": face_logins,
        "total_logins": total_logins,
        "history": history
    }