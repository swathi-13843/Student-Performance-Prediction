import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions(
id INTEGER PRIMARY KEY AUTOINCREMENT,
study_hours REAL,
attendance REAL,
previous_score REAL,
predicted_score REAL
)
""")

conn.commit()
conn.close()