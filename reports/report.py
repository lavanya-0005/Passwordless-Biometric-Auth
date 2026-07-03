import sqlite3
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from openpyxl import Workbook


def generate_pdf():

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username,
               method,
               status,
               login_time
        FROM login_history
    """)

    rows = cursor.fetchall()

    conn.close()

    data = [
        ["Username", "Method", "Status", "Login Time"]
    ]

    for row in rows:
        data.append(list(row))

    pdf = SimpleDocTemplate("reports/login_report.pdf")

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
        ])
    )

    pdf.build([table])

    return True


def generate_excel():

    conn = sqlite3.connect("database/users.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT username,
               method,
               status,
               login_time
        FROM login_history
    """)

    rows = cursor.fetchall()

    conn.close()

    wb = Workbook()

    ws = wb.active

    ws.title = "Login History"

    ws.append([
        "Username",
        "Method",
        "Status",
        "Login Time"
    ])

    for row in rows:
        ws.append(row)

    wb.save("reports/login_report.xlsx")

    return True