from database import database_read
from pprint import pprint


# Answer to 1st user story:
first_us = database_read(query='SELECT title, average_rating, year '
                               'FROM clean_books '
                               'WHERE valid_rating = 1 '
                               'GROUP BY year '
                               'ORDER BY year desc, average_rating desc '
                               'LIMIT 10')

# for book in first_us:
#     pprint(book)


# Answer to 2nd user story:
second_us = database_read(query='SELECT title, authors, text_reviews_count '
                                'FROM clean_books '
                                'ORDER BY text_reviews_count desc '
                                'LIMIT 10')

# for book in second_us:
#     pprint(book)


# Answer to 3rd user story:
third_us = database_read(query="SELECT COUNT(title) FROM clean_books "
                               "WHERE title LIKE '%Harry Potter%' AND "
                               "language_code = 'eng'")

# print(third_us[0])
