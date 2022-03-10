# %%
import pandas as pd
import os

myfile = 'books.csv'
path = os.path.join(os.getcwd(), myfile)

books = pd.read_csv(path, on_bad_lines='skip')

# %%

x = books.iloc[:, [1,8]]

print(x.sort_values(by=['ratings_count'], ascending=True))

print(x.ratings_count.describe())
# %%

books = books.head()

books.iloc[1:2, 8] = 59

print(books.iloc[:,8])

# %% 
def year(row):
    '''Returns the year from the publication_date column'''
    series = row['publication_date']
    pub_date = series.split('/')
    return pub_date[2]


def rating(row):
    '''Returns a True if ratings_count is bigger than 100'''
    print(row.ratings_count)
    if row.ratings_count >= 100:
        return True
    else:
        return False

books['year'] = books.apply(year,axis='columns')
books['valid_rating'] = books.apply(rating, axis='columns')

print(books)

# %%
