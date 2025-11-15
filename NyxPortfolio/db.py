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
cursor.execute('''INSERT INTO solves(solution, date, as_id) VALUES ("https://github.com/00nyx00/nyxportfolio/blob/3fc76cf12f1e184b28ffd8249f8566516ea9c10f/SQL/script.sql", "2025-11-14", 1)''')


conn.commit()
conn.close()

print("Database has been created yoohoo.")
