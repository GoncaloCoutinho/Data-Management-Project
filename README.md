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

I transformed the data using a pandas dataframe and ran some functions I made to unclean 25% of the dataset.
*(code can be found in the unclean.py file)*

## 3. User Stories

The following are the 3 user stories:
- As a librarian I want to know which are the top rated books by year so that I can make recommendations for our users.
- As a student I want to know which are the top 10 books that have the most text reviews so that I can study what leads to the most user engagement in books.
- As an historian I want to know which are the top 5 rated history books so that I can study them.
- As a fan of Harry Potter I would like to know how much does the whole collection of Harry Potter books costs?


## 4. Data profiling

The data profiling was done using the Talend Data Quality software. After running several column analysis and structural analysis I was able to qualify the quality dimensions of each column.

In order to use the software's more complex functions I had to create a MySQL database where I stored my unclean books dataframe.
*(code can be found in the database.py file)*

### Here are some examples of the analysis made:

*Checking functional dependency between bookID and title:*
![Functional Dependency]

*Checking for duplicates in title:*
![Simple Statistics]

*Making a pattern frequency analysis for language_code:*
![Pattern Frequency]

*Checking the range of average_rating:*
![Range Analysis]

### The analysis done is summarized in the following quality dimensions table:
| Columns | Primary key | Uniqueness | Completeness | Consistency | Accuracy | Conformity | Validity | Currency & Timeliness | Reliability & Credibility |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| book ID | Primary key (functional dependency) | Yes | Yes | Yes | - | - | Yes | - | Yes |
| title | - | - | Yes | No | Yes | Yes | Yes | - | Yes |
| authors | - | - | Yes | Yes | Yes | No | Yes | - | Yes |
| average_rating | - | - | Yes | Yes | No | Yes | No | No | Yes |
| isbn | Possible primary key (functional dependency) | Yes | Yes | Yes | - | - | Yes | - | Yes |
| isbn13 | Possible primary key (functional dependency) | Yes | Yes | Yes | - | - | Yes | - | Yes |
| language_code | - | - | Yes | No | Yes | No | Yes | - | Yes |
| num_pages | - | - | Yes | Yes | Yes | Yes | Yes | - | Yes |
| ratings_count | - | - | Yes | Yes | Yes | Yes | Yes | No | Yes |
| text_reviews_count | - | - | Yes | Yes | Yes | Yes | Yes | No | Yes |
| publication_date | - | - | Yes | No | Yes | No | Yes | - | Yes |
| publisher | - | - | Yes | Yes | Yes | No | Yes | - | Yes |
| year | - | - | Yes | Yes | Yes | Yes | No | - | Yes |
| valid_rating | - | - | Yes | No | Yes | No | No | No | Yes |
> Legend: 
`-` &#8594; quality dimension not relevant to column; 
`Yes` &#8594; quality dimension relevant to column and in check;
`No` &#8594; quality dimension relevant to column but not met.

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
   [Functional Dependency]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/bc993805-404c-4bf6-99f3-1b2a4d927cd8/data_profiling_functional_dependency.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T120853Z&X-Amz-Expires=86400&X-Amz-Signature=31ab8fcb30ff7c4b5748e47d5977d41400b87cc3b9cfb24021d27ba197c52f29&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_functional_dependency.png%22&x-id=GetObject
   [Simple Statistics]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/793a2f9d-9a22-46c1-a632-ee03efb42da7/data_profiling_2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T121324Z&X-Amz-Expires=86400&X-Amz-Signature=acc3c0931b778bdc6d1108c4b97dd88de85d08136fedbd5c52cd1fbd91b678d6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_2.png%22&x-id=GetObject
   [Pattern Frequency]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5640d5ea-435a-4f73-95f9-754ae294b566/data_profiling_pattern_frequency_analysis_language_code.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T120848Z&X-Amz-Expires=86400&X-Amz-Signature=8303a63cc8a0b9914a26c5c5ff9972f7aefc20d09b428912cb2106b50dbcf999&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_pattern_frequency_analysis_language_code.png%22&x-id=GetObject
   [Range Analysis]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e8aa87a5-0d93-455b-8122-2f974ae382bf/data_profiling_numerical_functions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T120845Z&X-Amz-Expires=86400&X-Amz-Signature=091b2bafabb26ccdf344ebfff6872b37718013c5db467bb42e66974e9afbc549&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22data_profiling_numerical_functions.png%22&x-id=GetObject
   