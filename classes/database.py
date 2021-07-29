import sqlite3
from sqlite3 import Error
from datetime import datetime


class Database:
    def __init__(self, path):
        self.connection = None
        try:
            self.connection = sqlite3.connect(path)
            print("SQLite Connected!")
        except Error as e:
            print(f"The error '{e}' occurred")

    def insert_ad(self, title, area, price, link):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        query = f"INSERT INTO ads (website, url, title, price, area, created) VALUES ('spitogatos.gr', '{link}', '{title}', '{price}', '{area}', '{dt_string}')"
        self.execute_query(query)

    def select_ad_with_url(self, ad_url):
        query = "SELECT id FROM ads WHERE url = " + str(ad_url)
        ads = self.execute_read_query(query)
        if len(ads) > 0:
            return ads[0]
        return None

    def execute_query(self, query=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query=None):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            return result

    def close_connection(self):
        self.connection.close()
