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

    result = cursor.execute(f'INSERT INTO {database}.docker_apps '\
                            f'(name, description) VALUES'\
                            f'("flask-app", "A simple web application writen in Flask."), '\
                            f'("database", "MySQL running in a container with a companion app.")')

    connection.commit()

    cursor.close()

    connection.close()

if __name__ == '__main__':

    load_dotenv('.env')

    database = os.environ['DATABASE']

    init_db(database)