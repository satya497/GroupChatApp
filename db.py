import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satya123",
    database="chat_app"
)
print(db)