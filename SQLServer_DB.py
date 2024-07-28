import pyodbc

# Define connection parameters
server = '127.0.0.1'  # The server name or IP address
database = 'intro'   # The database name
username = 'Muaaz'   # Your SQL Server username
password = 'your_password'   # Your SQL Server password

# Create a connection string
connection_string = f'''DRIVER={{ODBC Driver 17 for SQL Server}};
                    SERVER={server};
                    DATABASE={database};
                    UID={username};
                    PWD={password}'''

# Establish a connection to the database
connection = pyodbc.connect(connection_string)

# Create a cursor object
cursor = connection.cursor()

# INSERT statement
insert_query = """
INSERT INTO intro (name, age)
VALUES (?, ?);
"""

new_employee = ('Muaaz', 22)

cursor.execute(insert_query, new_employee)

# Define the SQL SELECT statement with a condition
select_query = '''SELECT name, age 
                FROM intro;'''

cursor.execute(select_query)

# Fetch all results from the executed query
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(f"Name: {row.name}, Age: {row.age} ")