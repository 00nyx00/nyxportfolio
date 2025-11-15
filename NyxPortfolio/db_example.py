import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS addresses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    address TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id)
                )''')

cursor.execute('''INSERT INTO users(name, age) VALUES ("claudia", 21)''')
cursor.execute('''INSERT INTO users(name, age) VALUES ("maria", 30)''')
cursor.execute('''INSERT INTO users(name, age) VALUES ("peter", 35)''')

cursor.execute('''INSERT INTO addresses(user_id, address) VALUES (1, "Street 123, City A")''')
cursor.execute('''INSERT INTO addresses(user_id, address) VALUES (2, "Street 456, City B")''')
cursor.execute('''INSERT INTO addresses(user_id, address) VALUES (3, "Street 789, City C")''')

# Update 
cursor.execute('''UPDATE users SET age = 22 WHERE name = "cladia"''')

# Delete 
cursor.execute('''DELETE FROM users WHERE name = "maria"''')

# Subquery
cursor.execute('''SELECT users.name, users.age, addresses.address
                  FROM users
                  JOIN addresses ON users.id = addresses.user_id
                  WHERE users.age > (SELECT AVG(age) FROM users)''')

# Get results and show
resultaten = cursor.fetchall()
for row in resultaten:
    print("Name:", row[0], "| Age:", row[1], "| Address:", row[2])

conn.commit()
conn.close()

print("Nice message of what you have done.")
