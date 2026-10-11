import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="yalini@2007",   # Replace with your MySQL password
        database="smart_waste_db"
    )