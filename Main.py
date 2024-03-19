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

def deleteStudent(student_id):
    """ Query 4: deleteStudent() - deletes the selected student from the students table
    """
    cursor.execute('DELETE FROM students WHERE student_id = %s', (student_id,))
    print("Student deleted")

if __name__ == '__main__':
    """ Entry point of the application
    """
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

        #Query 2
        first_name = "Matt"
        last_name = "Gaudet"
        email = "matt@email.com"
        date = "2023-09-03"
        print("Testing addStudent(matt, gaudet, matt@example.com, 2023-09-03)")
        addStudent(first_name, last_name, email, date) #email must be unique
        getAllStudents() #print the table
        
        #Query 3
        student_id_to_update = "2"
        new_email = "new_email@email.com"
        print("Testing updateStudentEmail(2, new_email@email.com)")
        updateStudentEmail(student_id_to_update, new_email)
        getAllStudents() #print the table
        
        #Query 4
        student_to_delete = 4
        print("Testing deleteStudent")
        deleteStudent(student_to_delete)
        getAllStudents() #print the table

        #cursor.execute('DELETE FROM students_test')

        #commit the changes
        conn.commit()
        cursor.close()
        conn.close()
    except psycopg.OperationalError as e:
        print(f"Error: {e}")
        exit(1)
