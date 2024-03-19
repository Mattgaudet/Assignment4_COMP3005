import psycopg
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = 5432

def deleteStudent(student_id):
    """ Query 4: deleteStudent() - deletes the selected student from the students table
    """
    cursor.execute('DELETE FROM students WHERE student_id = %s', (student_id,))
    print("Student deleted")

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
    #Query 4
    student_to_delete = 4
    print("Testing deleteStudent")
    deleteStudent(student_to_delete)
    
    #commit the changes
    conn.commit()
    cursor.close()
    conn.close()
except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)