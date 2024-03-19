import psycopg
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = 5432

def addStudent(first, last, email, enrollment_date):
    """ Query 2: addStudent() - adds a new student to the table
    """
    insert_data_query = '''
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        (%s, %s, %s, %s);
        '''
    data_to_insert = (first, last, email, enrollment_date)
    cursor.execute(insert_data_query, data_to_insert)
    print("Student added")

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
    #Query 2
    first_name = "Matt"
    last_name = "Gaudet"
    email = "matt@email.com"
    date = "2023-09-03"
    print("Testing addStudent(matt, gaudet, matt@example.com, 2023-09-03)")
    addStudent(first_name, last_name, email, date) #email must be unique
    
    #commit the changes
    conn.commit()
    cursor.close()
    conn.close()
except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)