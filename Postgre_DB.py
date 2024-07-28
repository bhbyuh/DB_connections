import psycopg2

#build connection with DB
conn = psycopg2.connect(
    dbname='company_info', #give your database name
    user="postgres",
    password='Muaaz123', # give your password
    host="localhost",
    port=5432
)

cur = conn.cursor()

#perform CRUD operations

#fecth data
cur.execute(f"""
    SELECT * from companies 
    WHERE  CR_number=1
    """)

rows=cur.fetchall()
for row in rows:
    print(row)

#insert data
cur.execute(f"""
            INSERT INTO companies (CR_number, company_name, email)
            VALUES (1, DataSwift, dataswift123@gmail.com)
        """)

conn.commit()