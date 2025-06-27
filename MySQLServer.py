import mysql.connector
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Makinde0604",
        database = "alx_book_store"
    )

except Exception as e:
    print("Unable to connect")
else:
    print("connected sucessfully")
    try:
        cursor = connection.cursor()
        cursor.execute("""CREATE DATABASE IF NOT EXISTS alx_book_store""")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DB_CREATE_EXISTS:
            print("Database 'alx_book_store' already exists.")
        else:
            print("Error",err)
finally:
    cursor.close()
    connection.close()


