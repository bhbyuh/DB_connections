import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('intro.db')

# Create a cursor object
cursor = connection.cursor()

# Define the SQL statement for creating a table
create_table_query = """
CREATE TABLE intro (
    age INTEGER,
    name TEXT
);
"""
cursor.execute(create_table_query)

# Define the SQL INSERT statement
insert_query = """
INSERT INTO employees (age,name)
VALUES (?, ?);
"""

employee_data = (22, 'Muaaz')

cursor.execute(insert_query, employee_data)
connection.commit()

# Define the SQL SELECT statement
select_query = "SELECT * FROM intro;"

cursor.execute(select_query)

rows = cursor.fetchall()

for row in rows:
    print(f"Age: {row[0]}, Name: {row[1]}")
