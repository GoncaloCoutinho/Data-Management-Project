# %%

import pandas as pd
import os

myfile = 'books.csv'
path = os.path.join(os.getcwd(), myfile)

books = pd.read_csv(path, on_bad_lines='skip')

print(books.head())

def unclean(df):
    """Returns a pandas DataFrame with 25% unclean data"""
    None

# %%
