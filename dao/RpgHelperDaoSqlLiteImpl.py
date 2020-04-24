from dao.RpgHelperDao import RpgHelperDao
import sqlite3
from sqlite3 import Error

""" 
    TODO: may want to initialize a connection within constructor and reference that within methods
"""


class RpgHelperDaoSqlLiteImpl(RpgHelperDao):
    def __init__(self, database_name):
        print(f"database {database_name} being initialized")
        self.database_name = database_name
        self.initialize_database()

    def add_inventory(self, user: str, channel: str, item: str):
        try:
            conn = self.create_connection(self.database_name)
            inventory_item = (user, channel, item)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT 
                INTO INVENTORY (
                    user,
                    channel,
                    item
                )
                VALUES (
                    ?,
                    ?,
                    ?
                )
                 """,
                           inventory_item)
            conn.commit()
            cursor.close()
        except Error as error:
            print(f'failure occurred inserting into inventory: {error}')
        finally:
            conn.close()

    @staticmethod
    def remove_inventory(self, user: str, item: str):
        print('This is not implemented')
        pass

    @staticmethod
    def add_stat(self, user: str, statName: str, value: int):
        print('This is not implemented')
        pass

    @staticmethod
    def update_stat(self, user: str, statName: str, value: int):
        print('This is not implemented')
        pass

    @staticmethod
    def remove_stat(self, user: str, statName: str):
        print('This is not implemented')
        pass

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as error:
            print(error)

        return conn

    def initialize_database(self):
        conn = self.create_connection(self.database_name)
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(""" CREATE TABLE IF NOT EXISTS inventory (
                                        user TEXT NOT NULL,
                                        channel TEXT NOT NULL,
                                        item TEXT NOT NULL
                                    ); """)
                conn.commit()
            except Error as error:
                print(error)
            finally:
                conn.close()
        else:
            print('could not establish database connection')
