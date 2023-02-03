from sqlalchemy import text
from src.utils.database_connection import connect, disconnect


class DBContext:
    connection = None

    def __init__(self) -> None:
        self.connection = connect()

    def execute(self, sql_text):
        return self.connection.execute(text(sql_text))

    def commit(self) -> None:
        self.connection.commit()

    def disconnect(self) -> None:
        disconnect(self.connection)
