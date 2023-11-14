import mysql.connector
from time import sleep
# from ..packages.textstyling import TextStyle


host = "127.0.0.1"
user = "root"
password = ""
database = "artofproblemsolving"

class TextStyle:
    __FAIL = "\033[91m"
    __WARNING = "\033[93m"
    
    __OKGREEN = "\033[92m"
    __OKBLUE = "\033[94m"
    __OKCYAN = "\033[96m"
    
    __HEADER = "\033[95m"
    __BOLD = "\033[1m"
    __UNDERLINE = "\033[4m"
    
    __ENDC = "\033[0m"
    
    def fail(self, text: str) -> str:
        return str(f"{self.__FAIL}{text}{self.__ENDC}")
    
    def warning(self, text: str) -> str:
        return str(f"{self.__WARNING}{text}{self.__ENDC}")
    
    def okgreen(self, text: str) -> str:
        return str(f"{self.__OKGREEN}{text}{self.__ENDC}")
    
    def okblue(self, text: str) -> str:
        return str(f"{self.__OKBLUE}{text}{self.__ENDC}")

    def okcyan(self, text: str) -> str:
        return str(f"{self.__OKCYAN}{text}{self.__ENDC}")
    
    def header(self, text: str) -> str:
        return str(f"{self.__HEADER}{text}{self.__ENDC}")

    def bold(self, text: str) -> str:
        return str(f"{self.__BOLD}{text}{self.__ENDC}")

    def underline(self, text: str) -> str:
        return str(f"{self.__UNDERLINE}{text}{self.__ENDC}")
    
    
bcolors = TextStyle()

def create_table(new_table_name: str):
    """
    This function will create new table 
    BUT IF IT'S ALREADY EXIST,
    the old record is not deleted.
    
    EVEN you change the table scenario
    """    

    print(bcolors.okblue("FUNCTION create_table()"))
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print(bcolors.okgreen('Connected to MySQL'))
            
            cursor = connection.cursor()
            query = f"""
                CREATE TABLE IF NOT EXISTS {new_table_name} (
                    id_key INT AUTO_INCREMENT PRIMARY KEY,
                    no VARCHAR(255),
                    contest_category VARCHAR(255),
                    contest_name VARCHAR(255),
                    year VARCHAR(255),
                    link TEXT,
                    pdf TEXT,
                    post_rendered TEXT,
                    post_canonical TEXT,
                    label VARCHAR(255)
                )
                """

            cursor.execute(query)
            print(bcolors.okgreen(f"Table \"{new_table_name}\" created successfully"))
            
    except mysql.connector.Error as error:
        print(f"{bcolors.fail('Error:')}\n{bcolors.fail(error)}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print(bcolors.warning("MySQL connection is closed") + "\n")


def insert_into(table: str, data: dict):

    print(bcolors.okblue("FUNCTION insert_into()"))
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            cursor = connection.cursor()
            
            query = f"""
                INSERT INTO `{table}`
                    (id_key, no, contest_category, contest_name, year, link, pdf, post_rendered, post_canonical, label)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            data_to_insert = (
                data['id_key'],
                data['no'],
                data['contest_category'],
                data['contest_name'],
                data['year'],
                data['link'],
                data['pdf'],
                data['post_rendered'],
                data['post_canonical'],
                data['label']
            )

            cursor.execute(query, data_to_insert)
            connection.commit()
            
            print(bcolors.okgreen(f"Row inserted successfully (id_key={data['id_key']})"))

    except mysql.connector.Error as error:
        print(f"{bcolors.fail('Error:')}\n{bcolors.fail(error)}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print(bcolors.warning("MySQL connection is closed") + "\n")


def edit_row():
    ...
    