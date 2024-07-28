from mysql import connector

# Establish a connection to the database
connection = connector.connect(
    host='127.0.0.1',        # Enter your host
    user='root',    
    password='Muaaz123?',    # Enter your password
    database='Intro'         # Name of the database to connect to
)
# Create a cursor object
cursor = connection.cursor()

# Create a table
create_table_query = '''
CREATE TABLE intro (
    name VARCHAR(255),
    age INT
)
'''
cursor.execute(create_table_query)

# Insert data
insert_query = '''
INSERT INTO employees (name, age) 
VALUES (%s, %s, %s)
'''
data = ("Muaaz", 22)
cursor.execute(insert_query, data)
connection.commit()

# Fetch data
select_query = "SELECT * FROM employees"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)