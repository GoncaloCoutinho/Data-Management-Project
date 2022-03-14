from dataset import books
import random
import string


def select_rows(df):
    """Selects 25% of the rows from a dataframe at random"""
    return df.sample(frac=0.25)


def check_missing_values(df):
    for col in df.columns:
        n_missing = df[col].isnull().sum()
        print(f"{n_missing} for {col}")


def unclean_title(df):
    sample = select_rows(df)
    return sample.title.str.upper()


def unclean_authors(df):
    """Returns a subset of 25% of the dataframe with a change to the authors
    column. Authors with more than 1 row get a random character appended to
    the end of their name in those additional rows."""
    sample = select_rows(df)

    # Select only authors that appear more than once
    uniques = sample.drop_duplicates(subset=['authors'])
    duplic = sample.loc[[d for d in sample.index if d not in uniques.index]]

    # Add random character to the end of the authors name
    random_char = random.choice(string.ascii_letters)
    x = duplic.authors.map(lambda s: s + random_char)

    return x


def unclean_avg_rat(df):
    """Returns a subset of 25% of the dataframe with the average_rating
    changed to a negative value"""
    sample = select_rows(df)
    sample['average_rating'] = -sample['average_rating']
    return sample


def unclean_lang_code(df):
    """Returns a subset of 25% of the dataframe with the language_code
    changed to a uppercase value"""
    sample = select_rows(df)
    return sample.language_code.str.upper()


def unclean_publisher(df):
    """Returns a subset of 25% of the dataframe with a change to the publisher
    column. Publishers with more than 1 row get a random character appended to
    the end of their name in those additional rows."""
    sample = select_rows(df)

    # Select only authors that appear more than once
    uniques = sample.drop_duplicates(subset=['publisher'])
    duplic = sample.loc[[d for d in sample.index if d not in uniques.index]]

    # Add random character to the end of the publishers name
    random_char = random.choice(string.ascii_letters)
    x = duplic.publisher.map(lambda s: s + random_char)

    return x


def unclean_year(df):
    """Returns a subset of 25% of the dataframe with the column year value
    increased by a random number between 1 to 10"""
    sample = select_rows(df)
    return sample.year.map(lambda y: int(y) + random.randint(1, 10))


def unclean_valid_rating(df):
    """Returns a subset of 25% of the dataframe with the column year value
    increased by a random number between 1 to 10"""
    sample = select_rows(df)
    sample = sample.valid_rating.astype('str')
    return sample.str.replace("True", "Yes").replace("False", "No")


def unclean(df):
    """Returns a pandas DataFrame with 25% unclean data"""
    df.update(unclean_authors(df))
    df.update(unclean_avg_rat(df))
    df.update(unclean_lang_code(df))
    df.update(unclean_publisher(df))
    df.update(unclean_year(df))
    df.update(unclean_title(df))
    df.update(unclean_valid_rating(df))

    return df


dirty_books = unclean(books)

# Save to new csv
if __name__ == '__main__':
    dirty_books.to_csv('dirty_books.csv', encoding='utf-8')
