import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chat_app"
)
print(db)