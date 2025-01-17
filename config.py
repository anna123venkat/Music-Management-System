import pymysql

# Database Configuration
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Prasanna3008"  # Update with your password
DB_NAME = "project"

# Establish a connection to the database
def get_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
