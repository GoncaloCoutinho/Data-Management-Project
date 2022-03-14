from unclean import dirty_books
from contextlib import contextmanager
import mysql.connector as msql
from mysql.connector import Error
from sqlalchemy import create_engine
import os


def setup_db():
    """Creates a table in the booksdb database in MySQL with the
    dirty_books dataframe from unclean.py"""
    # Set variables
    password = os.environ.get('MYSQL_PASS')
    user = 'root'
    db = 'booksdb'

    # Create sqlalchemy engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost/{db}")

    # Insert whole DataFrame into MySQL
    dirty_books.to_sql('books', con=engine, if_exists='append')


def database_read(query):
    with cursor_handler() as cur:
        cur.execute(query)
        rows = cur.fetchall()
    return rows


def execute_query(query):
    try:
        with cursor_handler() as cur:
            cur.execute(query)
    except Error as e:
        print(str(e))


@contextmanager
def cursor_handler():
    connection = msql.connect(host='localhost',
                              user='root',
                              password=os.environ.get('MYSQL_PASS'),
                              database='booksdb')
    cursor = connection.cursor()
    yield cursor
    cursor.close()
    connection.close()


if __name__ == "__main__":
    setup_db()
