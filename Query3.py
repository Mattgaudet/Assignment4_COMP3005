import psycopg
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = 5432

def updateStudentEmail(student_id, new_email):
    """ Query 3: updateStudentEmail() - updates the selected student's email
    """
    update_data_query = '''
    UPDATE students
    SET email = %s
    WHERE student_id = %t;
    '''
    data_to_insert = (new_email, student_id)
    cursor.execute(update_data_query, data_to_insert)
    print("Email updated")

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
    #Query 3
    student_id_to_update = "3"
    new_email = "new_email@email.com"
    print("Testing updateStudentEmail()")
    updateStudentEmail(student_id_to_update, new_email)
    
    #commit the changes
    conn.commit()
    cursor.close()
    conn.close()
except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)