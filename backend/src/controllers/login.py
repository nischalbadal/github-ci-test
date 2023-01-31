from src.db_context import DBContext

connection = DBContext()

# TODO : Update with actual logic
def verify_user():
    user = connection.execute("SELECT * FROM users")
    for row in user:
        print(row)
    connection.disconnect()


verify_user()
