import os
import mysql.connector

from dotenv import load_dotenv


def init_db(database):

    connection = mysql.connector.connect(
        host=os.environ['DBHOST'],
        user=os.environ['DBUSER'],
        password=os.environ['DBPASSWORD']
    )

    cursor = connection.cursor()

    cursor.execute(f'DROP DATABASE IF EXISTS {database}')
    cursor.execute(f'CREATE DATABASE {database}')

    cursor.execute(f'CREATE TABLE {database}.docker_apps ('\
                   f'name VARCHAR(100) NOT NULL,'\
                   f'description VARCHAR(255))')


if __name__ == '__main__':

    load_dotenv('.env')

    database = os.environ['DATABASE']

    init_db(database)