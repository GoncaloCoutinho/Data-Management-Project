# Data Management Project

## Introduction

This is an academic project focusing on data profiling and data cleaning.

These were the stages of the project:
1. Choose dataset;
2. Unclean the dataset to simulate real life scenarios of messy data;
3. Identify 3 user stories the dataset should answer;
4. Proceed with data profiling and build a quality dimensions table;
5. Clean the data;
6. Answer the user stories;

## 1. Dataset
I chose a books dataset that from kaggle ([link here][kaggle]).

I then added two columns to the dataset:
- year = year from the publication_date column;
- valid_rating = Boolean value &#8594; True if the ratings_count > 100 and text_reviews_count > 10. This will enable the exclusion of books with very few reviews when searching by highest average_rating.

*(code can be found in the dataset.py)*

This is a preview of the final dataset:
| bookID | title | authors | average_rating | isbn | isbn13 | language_code | num_pages | ratings_count | text_reviews_count | publication_date | publisher | year | valid_rating |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1	| Harry Potter and the Half-Blood Prince (Harry Potter  #6)	| J.K. Rowling/Mary GrandPré |	4.57 | 439785960 |	9.78044E+12 | eng |	652	| 2095690 |	27591 |	9/16/2006 |	Scholastic Inc. | 2006 | TRUE |
| 2 | Harry Potter and the Order of the Phoenix (Harry Potter  #5) | J.K. Rowling/Mary GrandPré | 4.49 | 439358078 | 9.78044E+12 | eng |	870 | 2153167 |	29221 |	09-01-04 | Scholastic Inc. | 2004 | TRUE |

## 2. Uncleaning 
I transformed the data using a pandas dataframe and running some functions I made to unclean 25% of the dataset.

*(code can be found in the unclean.py file)*

## 3. User Stories
The following are the 3 user stories:
- As a librarian I want to know which are the top rated books by year so that I can make recommendations for our users.
- As a student I want to know which are the top 10 books that have the most text reviews so that I can study what leads to the most user engagement in books.
- As an historian I want to know which are the top 5 rated history books so that I can study them.
- As a fan of Harry Potter I would like to know how much does the whole collection of Harry Potter books costs?


## 4. Data profiling 
The quality dimensions analyzed were the following

This is the quality dimensions table:
| Columns | Primary key | Uniqueness | Completeness | Consistency | Accuracy | Conformity | Validity | Currency | Timeliness | Reliability & Credibility |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| book ID |  |  |  |  |  |  |  |  |  |  |
| title |  |  |  |  |  |  |  |  |  |  |
| authors |  |  |  |  |  |  |  |  |  |  |
| average_rating |  |  |  |  |  |  |  |  |  |  |
| isbn |  |  |  |  |  |  |  |  |  |  |
| isbn13 |  |  |  |  |  |  |  |  |  |  |
| language_code |  |  |  |  |  |  |  |  |  |  |
| num_pages |  |  |  |  |  |  |  |  |  |  |
| ratings_count |  |  |  |  |  |  |  |  |  |  |
| text_reviews_count |  |  |  |  |  |  |  |  |  |  |
| publication_date |  |  |  |  |  |  |  |  |  |  |
| publisher |  |  |  |  |  |  |  |  |  |  |
| year |  |  |  |  |  |  |  |  |  |  |
| valid_rating |  |  |  |  |  |  |  |  |  |  |


## 5. Data Cleaning
The data cleaning was performed in OpenRefine.

This is the recipe used:
[PHOTO OF RECIPE]

Or link to the openrefine?

## 6. Answering the user stories
The file answers.py has all the queries that answer the user stories.
These where also performed in OpenRefine as seen below:
[PHOTO]

### Schema completeness
In order to complete the schema for my user cases the following columns had to be added to the dataset: year of publication, genre, non-fiction or fiction.

using the isbn code to get genre, check author and published date: (could also get a short description) [google][google search]

[//]: # (These are reference links they get stripped out when the markdown processor does its job)

   [kaggle]: <https://www.kaggle.com/jealousleopard/goodreadsbooks>
   [google search]: <https://www.google.de/search?q=isbn%3A+0471780936>
