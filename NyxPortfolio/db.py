import sqlite3

conn = sqlite3.connect('nyxportfolio.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS assignments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS solves (
                    solve_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    solution TEXT,
                    comments TEXT,
                    date DATE,
                    as_id INTEGER,
                    FOREIGN KEY (as_id) REFERENCES assignments(id)
                )''')

cursor.execute('''INSERT INTO assignments(name, description) VALUES ("2.1 SQL task", "tasks described in solution")''')
cursor.execute('''INSERT INTO solves(solution, date, as_id) VALUES ("https://github.com/code50/228491393/blob/12e1f329620de4866e37a6f262c9ad05398ed88d/SQL/script.sql", 2025-11-14, 1)''')



'''
# Get results and show
results = cursor.fetchall()
for row in results:
    print("Name:", row[0], "| Age:", row[1], "| Address:", row[2])
'''
conn.commit()
conn.close()

print("Nice message of what you have done.")
