import  mysql.connector
import Creds
from mysql.connector import Error
from TWsql import create_con
from TWsql import execute_query
from TWsql import execute_read_query

#create a connection to mysql database
myCreds = Creds.Creds()
conn = create_con(myCreds.conString, myCreds.userName, myCreds.password, myCreds.databaseName)

#create a new entry and add it to the table
#query = "INSERT INTO users (firstname, lastname) Values ('Thomas', 'Edison')"
#execute_query(conn, query)

#select all users
select_users = 'SELECT * FROM users'
users = execute_read_query(conn, select_users)
for user in users:
    print(user)
    print(user["firstname"] + " has the last name " + user["lastname"])

create_invoice_table = """
CREATE TABLE IF NOT EXISTS invoices(
    id INT AUTO_INCREMENT,
    amount INT,
    description VARCHAR(255) NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY fk_user_id(user_id) REFERENCES users(id),
    PRIMARY KEY (id)
)"""
execute_query(conn,create_invoice_table)

#add an invoice record to the invoice table
invoice_from_user = 1
invoice_amount = 50
invoice_description = "Harry Potter Books"

query = "INSERT INTO invoices (amount, description, user_id) VALUES (%s, '%s', %s)" % (invoice_amount, invoice_description, invoice_from_user)

#execute_query(conn, query)

#update invoice record
new_amount = 30
update_invoice_query = """
UPDATE invoices
SET amount = %s
WHERE id = 1""" % (new_amount)

#execute_query(conn, update_invoice_query)

#delete invoice record from invoice table
invoice_to_delete = 1
delete_statement = "DELETE FROM invoices WHERE id = %s" % (invoice_to_delete)
#execute_query(conn, delete_statement)

#delete invoice table
delete_table_statement = "DROP TABLE invoices"
execute_query(conn, delete_table_statement)

#concludes CRUD OPS