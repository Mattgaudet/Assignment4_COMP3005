import psycopg
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_PORT = 5432

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

    #create the database 
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            enrollment_date DATE
        );
        '''

    #execute the SQL statement
    cursor.execute(create_table_query)
    print("Database table created")

    #insert data
    insert_data_query = '''
        INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
        ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
        ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
        ('Jim', 'Bean', 'jim.beam@example.com', '2023-09-02');
        '''

    #execute the SQL statement
    cursor.execute(insert_data_query)
    print("Data inserted into table")

    #commit the changes
    conn.commit()
    cursor.close()
    conn.close()
    
except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)