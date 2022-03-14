from database import setup_db
import pandas as pd
import os

# Create Dataframe
myfile = 'clean_books.csv'
path = os.path.join(os.getcwd(), myfile)
clean_books = pd.read_csv(path, on_bad_lines='skip', encoding='utf-8')

setup_db(df=clean_books, name='clean_books')
