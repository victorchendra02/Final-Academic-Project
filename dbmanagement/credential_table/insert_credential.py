import mysql.connector
from mysql.connector import errorcode


def create_database():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=""
    )

    cursor = connection.cursor()
    database_name = 'aopsimol_artofproblemsolving'

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

    cursor.close()
    connection.close()
    
def create_table():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database = "aopsimol_artofproblemsolving"
    )

    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS `credential_table` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `datetime` timestamp NULL DEFAULT NULL,
        `credential` varchar(255) DEFAULT NULL,
        `is_active` tinyint(1) DEFAULT NULL,
        PRIMARY KEY (`id`),
        UNIQUE KEY `credential` (`credential`)
        );
    """

    cursor.execute(query)

    cursor.close()
    connection.close()

def insert_row(credential, is_active):
    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="aopsimol_artofproblemsolving"
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert data into the table
        query = "INSERT INTO `credential_table` (`datetime`, `credential`, `is_active`) VALUES (NOW(), %s, %s)"
        data = (credential, is_active)
        cursor.execute(query, data)

        # Commit the changes to the database
        connection.commit()

        print("Row inserted successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print("Error:", err)

    finally:
        # Close the cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def read_txt(file_path):
    """
    NOTE: Return list
    """
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            result = content.split("\n")

            return result

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    credential_list = read_txt("credential_list.txt")
    
    create_database()
    create_table()
    for cred in credential_list:
        insert_row(cred, 1)
