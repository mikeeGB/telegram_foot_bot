import psycopg2
from configuration.config import DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT


class DBManager:
    """Class for managing postgresql database"""
    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        """Initializing fields for connection"""
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    def create_connection(self):
        """Creating connection to PostgreSQL"""
        connection = None

        try:
            connection = psycopg2.connect(
                database=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port,
            )
            print(f"Connected to PostgreSQL {self.db_name} successfully")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection

    @staticmethod
    def execute_read_query(connection, query):
        """Reading data from tables"""
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
        except psycopg2.Error as e:
            print(f"The error '{e}' occurred")
        else:
            return result

    @staticmethod
    def execute_query(connection, query):
        """Method for creating tables, inserting, updating and deleting"""
        # connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Query executed successfully")
        except psycopg2.OperationalError as e:
            print(f"The error '{e}' occurred")


dbman = DBManager(DB_NAME, DB_USER, DB_PASS, DB_HOST, DB_PORT)