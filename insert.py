import sqlite3

conn = sqlite3.connect ('my_database.db')
cursor = conn.cursor()
query = """
INSERT TWO points (x,y)
VALUES (2,3);

    """
    cursor.execute(query)
    conn.commit()
    conn.close()