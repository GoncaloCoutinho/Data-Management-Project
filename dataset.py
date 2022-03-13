import pandas as pd
import os


def year(row):
    '''Returns the year from the publication_date column'''
    series = row['publication_date']
    pub_date = series.split('/')
    return pub_date[2]


def rating(row):
    '''Returns a True if ratings_count is bigger than 100 and
    text_reviews_count bigger than 10'''
    if row.ratings_count > 100 and row.text_reviews_count > 10:
        return True
    else:
        return False


# Create Dataframe
myfile = 'books.csv'
path = os.path.join(os.getcwd(), myfile)
books = pd.read_csv(path, on_bad_lines='skip')

# Add new columns, set index and remove whitespaces from col names
books['year'] = books.apply(year, axis='columns')
books['valid_rating'] = books.apply(rating, axis='columns')
books.set_index('bookID', inplace=True)
books.columns = books.columns.str.lstrip()

# Save to new csv
if __name__ == '__main__':
    books.to_csv('new_books.csv')
