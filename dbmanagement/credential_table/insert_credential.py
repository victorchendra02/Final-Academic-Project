import mysql.connector
from mysql.connector import errorcode


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

    for cred in credential_list:
        insert_row(cred, 1)
