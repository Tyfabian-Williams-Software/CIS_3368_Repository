import  mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpw,
            database = dbname
        )
        print("Connection to MysQL Successful")
    except Error as e:
        print(f'The error {e} occured')
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query printed succefully")
    except Error as e:
        print(f'The error {e} occured')
              
def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary = True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f'The error {e} occured')