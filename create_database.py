from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


def create_db(database_uri):
    engine = create_engine(database_uri)
    connection = engine.connect()
    if(connection):
        connection.execute("commit")
        try:
            connection.execute('create database un_saikiran')
            print('\nDatabase un_saikiran created successfully\n')
        except Exception:
            print('\nDatabase un_saikiran already Exists.\n')
        finally:
            connection.close()
    else:
        print('\nConnection failed. Verify credentials\n')


if(__name__ == '__main__'):
    load_dotenv()
    username = os.getenv("username")
    password = os.getenv("password")
    database_uri = f'postgres://{username}:{password}@localhost'
    create_db(database_uri)
