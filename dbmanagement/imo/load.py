import pandas as pd
import mysql.connector
from time import sleep


class TextStyle:
    FAIL = "\033[91m"
    WARNING = "\033[93m"
    
    OKGREEN = "\033[92m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    
    HEADER = "\033[95m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    ENDC = "\033[0m"
    
    def fail(self, text: str) -> str:
        return str(f"{self.FAIL}{text}{self.ENDC}")
    
    def warning(self, text: str) -> str:
        return str(f"{self.WARNING}{text}{self.ENDC}")
    
    def okgreen(self, text: str) -> str:
        return str(f"{self.OKGREEN}{text}{self.ENDC}")
    
    def okblue(self, text: str) -> str:
        return str(f"{self.OKBLUE}{text}{self.ENDC}")

    def okcyan(self, text: str) -> str:
        return str(f"{self.OKCYAN}{text}{self.ENDC}")
    
    def header(self, text: str) -> str:
        return str(f"{self.HEADER}{text}{self.ENDC}")

    def bold(self, text: str) -> str:
        return str(f"{self.BOLD}{text}{self.ENDC}")

    def underline(self, text: str) -> str:
        return str(f"{self.UNDERLINE}{text}{self.ENDC}")
    
    
class MySQLDBManager:
    # For `Wampserver64`
    def __init__(self, host="127.0.0.1", user="root", password="", database="aopsimol_artofproblemsolving") -> None:
        self.bcolors = TextStyle()
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()
        
    def create_database(self, dbname):
        print(self.bcolors.okblue(f"[FUNCTION CALLED] --> create_database()"))
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbname};")
            print(
                self.bcolors.okgreen(f'Database "{dbname}" created successfully.')
            )
        except mysql.connector.Error as err:
            print(
                self.bcolors.fail(f"Error: {err}")
            )

    def use_database(self, database_name):
        print(self.bcolors.okblue(f"[FUNCTION CALLED] --> use_database()"))
        try:
            self.cursor.execute(f"USE {database_name}")
            print(f"Using database '{database_name}'.")
        except mysql.connector.Error as err:
            print(
                self.bcolors.fail(f"Error: {err}")
            )

    def create_table(self, table_name):
        print(self.bcolors.okblue(f"[FUNCTION CALLED] --> create_table()"))
        try:
            create_table_query = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id_key INT AUTO_INCREMENT PRIMARY KEY,
                    no VARCHAR(255),
                    contest_category VARCHAR(255),
                    contest_name VARCHAR(255),
                    year INT,
                    link TEXT,
                    pdf TEXT,
                    post_rendered TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
                    post_canonical TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
                    label VARCHAR(255)
                )
                """
            self.cursor.execute(create_table_query)
            print(
                self.bcolors.okgreen(f"Table '{table_name}' created successfully.")
            )
        except mysql.connector.Error as err:
            print(
                self.bcolors.fail(f"Error: {err}")
            )

    def insert_into(self, tname, data_to_insert: tuple): 
        try:
            query = f"""
                INSERT INTO `{tname}`
                    (id_key, no, contest_category, contest_name, year, link, pdf, post_rendered, post_canonical, label)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            data = (
                data_to_insert['id_key'],
                data_to_insert['no'],
                data_to_insert['contest_category'],
                data_to_insert['contest_name'],
                data_to_insert['year'],
                data_to_insert['link'],
                data_to_insert['pdf'],
                data_to_insert['post_rendered'],
                data_to_insert['post_canonical'],
                data_to_insert['label']
            )
            self.cursor.execute(query, data)
            print(
                self.bcolors.okgreen((data_to_insert["no"], data_to_insert["year"], data_to_insert["link"]))
            )
        except mysql.connector.Error as err:
            print(
                self.bcolors.warning((data_to_insert["no"], data_to_insert["year"], data_to_insert["link"]))
            )
            print(
                self.bcolors.fail(f"Error: {err}")
            )
            sleep(2)
        
    def close_connection(self):
        print(self.bcolors.okblue(f"[FUNCTION CALLED] --> close_connection()"))
        self.cursor.close()
        self.connection.close()
        print(
            self.bcolors.warning("MySQL connection is closed")
        )
    
    def initialize(self, path: str):
        print(self.bcolors.okblue(f"[FUNCTION CALLED] --> initialize()"))
        
        self.create_database(self.database)
        self.use_database(self.database)
        self.create_table("imo")
        
        df = pd.read_csv(path)
        num_rows = df.shape[0]
        for i in range(num_rows):
            data_to_insert = df.loc[i].to_dict()
            if type(data_to_insert['label']) == float:
                data_to_insert['label'] = None

            self.insert_into("imo", data_to_insert)
            # sleep(0.01)
        
        self.close_connection()


if __name__ == '__main__':
    # How to run:
    # CTRL + SHIFT + C
    # conda activate artofproblemsolving
    # cd dbmanagement
    # cd imo
    # python -u load.py
    
    host = "127.0.0.1"
    user = "root"
    password = ""
    database = "aopsimol_artofproblemsolving"
    
    path = '../../data/classification/imo.csv'
    db = MySQLDBManager(host, user, password, database)
    db.initialize(path)
    