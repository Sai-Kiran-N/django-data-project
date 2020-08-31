from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


def drop_database(database_uri):
    engine = create_engine(database_uri)
    connection = engine.connect()
    if(connection):
        connection.execute("commit")
        connection.execute('drop database if exists un_saikiran')
        print('\nDatabase un_saikiran dropped successfully\n')
        connection.close()
    else:
        print('\nConnection failed.verify credentials\n')


if(__name__ == '__main__'):
    load_dotenv()
    username = os.getenv("username")
    password = os.getenv("password")
    database_uri = f'postgres://{username}:{password}@localhost'
    drop_database(database_uri)
