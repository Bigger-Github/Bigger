import psycopg2
from psycopg2 import sql

DATABASE = "ss"
USER = "postgres"
PASSWORD = "pgAdmin4"
HOST = "localhost"  
PORT = "5432"  

conn = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
cursor = conn.cursor()

def read_data(student_number):
    try:
        cursor.execute("SELECT * FROM student WHERE sno = %s;", (student_number,))
        student = cursor.fetchone()
        if student:
            print(student)
        else:
            print("No student found with that number.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()

def insert_data(student_number, name, age, gender, department_name):
    try:
        cursor.execute("SELECT * FROM student WHERE sno = %s;", (student_number,))
        if cursor.fetchone():
            print("Student number already exists. Please re-enter.")
        else:
            cursor.execute("INSERT INTO student (sno, sname, sage, sgender, sdept) VALUES (%s, %s, %s, %s, %s);",
                           (student_number, name, age, gender, department_name))
            conn.commit()
            print("Student data inserted successfully.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()

def update_data(student_number, new_name, new_age, new_gender, new_department_name):
    try:
        cursor.execute("SELECT * FROM student WHERE sno = %s;", (student_number,))
        if cursor.fetchone():
            cursor.execute("UPDATE student SET sname=%s, sage=%s, sgender=%s, sdept=%s WHERE sno = %s;",
                           (new_name, new_age, new_gender, new_department_name, student_number))
            conn.commit()
            print("Student data updated successfully.")
        else:
            print("Student not found.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()

def delete_data(student_number):
    try:
        cursor.execute("SELECT * FROM sc WHERE sno = %s;", (student_number,))
        if cursor.fetchall():
            cursor.execute("DELETE FROM sc WHERE sno = %s;", (student_number,))
            conn.commit()
            print("Student's course enrollment records deleted.")

        cursor.execute("DELETE FROM student WHERE sno = %s;", (student_number,))
        if cursor.rowcount > 0:
            conn.commit()
            print("Student data deleted successfully.")
        else:
            print("No student found with that number to delete.")
    except psycopg2.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()





    finally:
       

       cursor.close()
       conn.close()




# A1 = read_data('20200001')
# A2 = insert_data('20200011', 'WangYizhou', 21, 'M', 'cs')
# A3 = update_data('20200011', 'Wang new', 21, 'M', 'cs')
A4 = delete_data('20200001')