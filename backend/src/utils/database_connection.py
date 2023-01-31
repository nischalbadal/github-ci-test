import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()


def connect():
    db_url = os.getenv("DB_CONNECTION_STRING")

    try:
        engine = create_engine(db_url)
        session = sessionmaker(bind=engine)()
        connection = session.connection()
        return connection
    except Exception as e:
        print("[-] Exception Occurred:", e)
        return None


def disconnect(connection):
    try:
        connection.close()
    except Exception as e:
        print("[-] Exception Occurred:", e)
