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
        print("CONN SUCCESSFUL")
    except Error as e:
        print(f'The error {e} occured')
    return connection

conn = create_con('', '', '', '')
cursor = conn.cursor(dictionary = True)
sql = 'SELECT * FROM users'
cursor.execute(sql)
rows = cursor.fetchall()
for user in rows:
    print(user)
    print('first name is: ' + user['firstname'])
