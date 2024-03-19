import psycopg
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = 5432

def getAllStudents():
    """ Query 1: getAllStudents() - prints the students table
    """
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

try:
    #connect to the database
    conn = psycopg.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    #create a cursor
    cursor = conn.cursor()
    print("Cursor created")

    #Test queries here
    #Query 1
    print("Testing getAllStudents()")
    getAllStudents() #print the table

    #commit the changes
    conn.commit()
    cursor.close()
    conn.close()
except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)
