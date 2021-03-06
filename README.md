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

I chose a books dataset from kaggle found [here][kaggle].

I then added two columns to the dataset:
- year = year from the publication_date column;
- valid_rating = Boolean value &#8594; True if the ratings_count > 100 and text_reviews_count > 10. This will enable the exclusion of books with very few reviews when searching by highest average_rating.

> *code can be found in the dataset.py*

This is a preview of the final dataset:
| bookID | title | authors | average_rating | isbn | isbn13 | language_code | num_pages | ratings_count | text_reviews_count | publication_date | publisher | year | valid_rating |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 1	| Harry Potter and the Half-Blood Prince (Harry Potter  #6)	| J.K. Rowling/Mary GrandPré |	4.57 | 439785960 |	9.78044E+12 | eng |	652	| 2095690 |	27591 |	9/16/2006 |	Scholastic Inc. | 2006 | TRUE |
| 2 | Harry Potter and the Order of the Phoenix (Harry Potter  #5) | J.K. Rowling/Mary GrandPré | 4.49 | 439358078 | 9.78044E+12 | eng |	870 | 2153167 |	29221 |	09-01-04 | Scholastic Inc. | 2004 | TRUE |

## 2. Uncleaning 

I transformed the data using a pandas dataframe and ran functions to unclean 25% of the dataset.

Each uncleaning function was applied to a column on a 25% sample of the dataframe. Afterwards the dataframe was updated with the new values returned by each function.

Each function used a different sample, guaranteeing that at the very least 25% of the rows in the data have some unclean column.

Here is an example of a function that modifies the column title to all uppercase, thus affecting the consistency dimension:

```python
def unclean_title(df):
    sample = select_rows(df)
    return sample.title.str.upper()
```

> *code can be found in the unclean.py file*

## 3. User Stories

The following are the 3 user stories:
- As a librarian I want to know which are the top rated books by year for the last 10 years so that I can make recommendations to our users.
- As a student I want to know which are the top 10 books and respective authors that have the most text reviews so that I can study what leads to the most user engagement in books.
- As a new fan of Harry Potter I would like to know how many Harry Potter related books exist in english.


## 4. Data profiling

The data profiling was done using the Talend Data Quality software. After running several column analysis and structural analysis I was able to qualify the quality dimensions of each column.

In order to use the software's more complex functions I had to create a MySQL database where I stored my unclean books dataframe.

> *code can be found in the database.py file*

### Here are some examples of the analysis made:

*Checking functional dependency between bookID and title:*
![Functional Dependency]

*Checking for duplicates in title:*
![Simple Statistics]

*Making a pattern frequency analysis for language_code:*
![Pattern Frequency]

*Checking the range of average_rating:*
![Range Analysis]

### Quality dimensions table:
Following the analysis done the data quality was performed using a **quality dimension wise approach**, this is, for each quality dimension I analyzed it for all the columns.
| Columns | Primary key | Uniqueness | Completeness | Consistency | Accuracy | Conformity | Validity | Currency & Timeliness | Reliability & Credibility |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| book ID | Primary key | Yes | Yes | Yes | - | - | Yes | - | Yes |
| title | - | - | Yes | No | Yes | Yes | Yes | - | Yes |
| authors | - | - | Yes | Yes | Yes | No | Yes | - | Yes |
| average_rating | - | - | Yes | Yes | No | Yes | No | No | Yes |
| isbn | Possible primary key | Yes | Yes | Yes | - | - | Yes | - | Yes |
| isbn13 | Possible primary key | Yes | Yes | Yes | - | - | Yes | - | Yes |
| language_code | - | - | Yes | No | Yes | No | Yes | - | Yes |
| num_pages | - | - | Yes | Yes | Yes | Yes | Yes | - | Yes |
| ratings_count | - | - | Yes | Yes | Yes | Yes | Yes | No | Yes |
| text_reviews_count | - | - | Yes | Yes | Yes | Yes | Yes | No | Yes |
| publication_date | - | - | Yes | No | Yes | No | Yes | - | Yes |
| publisher | - | - | Yes | Yes | Yes | No | Yes | - | Yes |
| year | - | - | Yes | Yes | Yes | Yes | No | - | Yes |
| valid_rating | - | - | Yes | No | Yes | No | No | No | Yes |
> **Legend**:
>
> `-` &#8594; quality dimension not relevant to column;
>
> `Yes` &#8594; quality dimension relevant to column and in check;
>
> `No` &#8594; quality dimension relevant to column but not met.

## 5. Data Cleaning

The data cleaning was performed in OpenRefine.

### Here are some examples of cleaning steps made:

*Clustering algorithm to achieve conformity in the authors column:*
![Clustering]

*Regular expression to achieve conformity and consistency in the language_code column:*
![regular expression]

*If statement to achieve validity in the year column:*
![year_transformation]

*Absolute value transformation to achieve validity in the year column:*
![average_rating]

### Recipe

> *The full recipe can be found in the recipe.json file.* 

## 6. Answering the user stories

The cleaning data was put into MySQL in another table called clean_books.

> *Code can be found in the clean_database.py file.* 

Afterwards I proceeded to answer the user stories with SQL queries.

### User stories and answers:

- 1st User Story &#8594; As a librarian I want to know which are the top rated books by year for the last 10 years so that I can make recommendations to our users.

These are the top books by each year considering the dataset was collected until December 8th, 2020:

![top rated books by year]

>To answer this user-story, the dimensions consistency was considered for the column “title”, validity + accuracy "year" and validity + accuracy + currency for "average_rating"

---

- 2nd User Story &#8594; As a student I want to know which are the top 10 books and respective authors that have the most text reviews so that I can study what leads to the most user engagement in books.

These are the top books by text review count considering the dataset was collected until December 8th, 2020:

![top text reviewed books]

>To answer this user-story, the dimensions conformity + consistency was considered for the column “authors”, consistency for the column "title" and currency for the "text_reviews_count"

---

- 3rd User Story &#8594; As a new fan of Harry Potter I would like to know how many Harry Potter related books exist in english.

The number of Harry Potter related books with language in english, as of December 8th 2020 is 18:

![harry potter book count]

>To answer this user-story, the dimensions conformity + consistency was considered for the column “language_code”.

---

> *All the queries can be found in the answers.py file.* 

[//]: # (These are reference links they get stripped out when the markdown processor does its job)

   [OpenRefine Permalink]: <http://127.0.0.1:3333/project?project=1706991223211&ui=%7B%22facets%22%3A%5B%5D%7D>
   [kaggle]: <https://www.kaggle.com/jealousleopard/goodreadsbooks>
   [google search]: <https://www.google.de/search?q=isbn%3A+0471780936>
   [Functional Dependency]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/bc993805-404c-4bf6-99f3-1b2a4d927cd8/data_profiling_functional_dependency.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T124626Z&X-Amz-Expires=86400&X-Amz-Signature=fab40227010c9f0599e69c10ec26dc307f715e99a252f0ca0aa52a0455b343c6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_functional_dependency.png%22&x-id=GetObject
   [Simple Statistics]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/793a2f9d-9a22-46c1-a632-ee03efb42da7/data_profiling_2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T124638Z&X-Amz-Expires=86400&X-Amz-Signature=ee62c5dbf8ea1e6997770306f20111c9dbc00cd3e3a27334c1836c5e4447551b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_2.png%22&x-id=GetObject
   [Pattern Frequency]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5640d5ea-435a-4f73-95f9-754ae294b566/data_profiling_pattern_frequency_analysis_language_code.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T124629Z&X-Amz-Expires=86400&X-Amz-Signature=9872c23f7185ac52c553127d2078f7ae8259db68cad5a88b4047b63ca101b25a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_pattern_frequency_analysis_language_code.png%22&x-id=GetObject
   [Range Analysis]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e8aa87a5-0d93-455b-8122-2f974ae382bf/data_profiling_numerical_functions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T124634Z&X-Amz-Expires=86400&X-Amz-Signature=cd8d05324678d3ca36cbd5f798d9ede622823d19ab1c04cb2b270cdcf25ce3c6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_numerical_functions.png%22&x-id=GetObject
   [Clustering]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6b2c2542-b4f3-43d4-8fc4-e3fe6461495c/data_cleaning_clustering.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T132006Z&X-Amz-Expires=86400&X-Amz-Signature=f3f28da61e4ad01e7520e7a804185a8d7dffc453d9ba5bf1c5c97f5b49f3812f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_cleaning_clustering.png%22&x-id=GetObject
   [year_transformation]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/91ba6510-ee3b-4e1b-97af-7997f1f06195/data_cleaning_year.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T170538Z&X-Amz-Expires=86400&X-Amz-Signature=84a3d010ca1f17c1b4c7372397d24769ca3e810ca38d1e30db9f333ac6d7b370&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_cleaning_year.png%22&x-id=GetObject
   [average_rating]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e9efa84e-80d7-4533-8fed-3f7eb4ab0554/data_cleaning_absolute.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T170535Z&X-Amz-Expires=86400&X-Amz-Signature=86d037cefb310ee06fdfbe1ee3c69c4d23afed9f0f8be2d74f01c0cce73c80c2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_cleaning_absolute.png%22&x-id=GetObject
   [regular expression]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f9173df2-ef9d-41be-8893-7592c8fababd/data_cleaning_language_code.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T170531Z&X-Amz-Expires=86400&X-Amz-Signature=ce38577bb98dbb792a10482d72ed4c208d0084af84827e8de579a85db2a88863&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_cleaning_language_code.png%22&x-id=GetObject
   [top rated books by year]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a560fe56-324f-4a64-8ac0-e1c9c9a8df93/top_rated_books_by_year.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T182934Z&X-Amz-Expires=86400&X-Amz-Signature=8c4916b7ac598122f95e5d51e8cf905802b77a8575b4a42324db40d4af2f6abb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22top_rated_books_by_year.png%22&x-id=GetObject
   [top text reviewed books]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3f85fea2-df2c-4791-8024-f5e5ba04e49d/top_text_reviewed_books.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T182931Z&X-Amz-Expires=86400&X-Amz-Signature=000435be5780a38dd6651eaca523206ec6a737fbb44c2578c75940a4047cc0ba&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22top_text_reviewed_books.png%22&x-id=GetObject
   [harry potter book count]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8750621c-4584-4084-8e68-85c81b2d32d6/how_many_harry_potter_books.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T182929Z&X-Amz-Expires=86400&X-Amz-Signature=d2a52d5c5d1ce91627463b08aba99f9623debc868d3a262266f70621c196771b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22how_many_harry_potter_books.png%22&x-id=GetObject
