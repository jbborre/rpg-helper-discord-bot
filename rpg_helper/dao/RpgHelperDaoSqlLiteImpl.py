from rpg_helper.dao.RpgHelperDao import RpgHelperDao
import sqlite3
from sqlite3 import Error
import logging
from typing import List
from rpg_helper.models.Inventory import Inventory
InventoryList = List[Inventory]

""" 
    TODO: may want to initialize a connection within constructor and reference that within methods
"""


class RpgHelperDaoSqlLiteImpl(RpgHelperDao):
    def __init__(self, database_name):
        logging.info(msg=f"database {database_name} being initialized")
        self.database_name = database_name
        self.initialize_database()

    def add_inventory(self, user: str, user_id: str, channel_id: str, item: str):
        try:
            conn = self.create_connection(self.database_name)
            inventory_item = (user, user_id, channel_id, item)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT 
                INTO INVENTORY (
                    user,
                    user_id,
                    channel_id,
                    item
                )
                VALUES (
                    ?,
                    ?,
                    ?,
                    ?
                )
                 """,
                           inventory_item)
            conn.commit()
            cursor.close()
        except Error as error:
            logging.error(msg=f'failure occurred inserting into inventory: {error}')
        finally:
            conn.close()

    def get_user_inventory(self, user_id: str, channel_id: str) -> InventoryList:
        try:
            conn = self.create_connection(self.database_name)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT user,
                    user_id,
                    channel_id,
                    item 
                FROM INVENTORY 
                WHERE USER_ID=? 
                AND CHANNEL_ID=?""",
                           (user_id, channel_id))
            rows = cursor.fetchall()
            logging.info(f'rows: {rows}')

            def resolver(row):
                return Inventory(user_id=row[2], item=row[3])

            return list(map(resolver, rows))
        except Error as error:
            logging.error(msg=f'failure occurred getting inventory for user: {error}')
        finally:
            conn.close()

    def remove_inventory(self, channel_id: str, user_id: str, item: str):
        logging.error(msg='This is not implemented')
        pass

    def add_stat(self, channel_id: str, user_id: str, stat_name: str, value: int):
        logging.error(msg='This is not implemented')
        pass

    def update_stat(self, channel_id: str, user_id: str, stat_name: str, value: int):
        logging.error(msg='This is not implemented')
        pass

    def remove_stat(self, channel_id: str, user_id: str, stat_name: str):
        logging.error(msg='This is not implemented')
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
            logging.error(msg=f'failure creating a connection to the database: {error}')

        return conn

    def initialize_database(self):
        conn = self.create_connection(self.database_name)
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute(""" CREATE TABLE IF NOT EXISTS inventory (
                                        user TEXT NOT NULL,
                                        user_id TEXT NOT NULL,
                                        channel_id TEXT NOT NULL,
                                        item TEXT NOT NULL
                                    ); """)
                cursor.execute(""" CREATE INDEX chan_user_inv
                                    ON inventory(channel_id, user_id); 
                                    """)
                conn.commit()
            except Error as error:
                logging.error(msg=f'failure creating the database: {error}')
            finally:
                conn.close()
        else:
            logging.error(msg='could not establish database connection')
