import sqlite3


def get_all_users():

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,
               username,
               created_at
        FROM users
        ORDER BY id ASC
    """)

    users = cursor.fetchall()

    conn.close()

    return users


def delete_user(user_id):

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    # Get username first
    cursor.execute(
        "SELECT username FROM users WHERE id=?",
        (user_id,)
    )

    row = cursor.fetchone()

    if row:

        username = row[0]

        # Delete login history
        cursor.execute(
            "DELETE FROM login_history WHERE username=?",
            (username,)
        )

        # Delete user
        cursor.execute(
            "DELETE FROM users WHERE id=?",
            (user_id,)
        )

    conn.commit()
    conn.close()