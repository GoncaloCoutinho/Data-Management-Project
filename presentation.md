---
marp: true
theme: default
_class: invert
---

# Books Analysis 

![bg right h:500 h:600][goodreads]

Data profiling and cleaning of a data set about books


---

<!-- footer: 'Data Management 1 • Professors: Prof. Dr. Ajinkya Prabhune, Prof. Ashish Chouhan • Student: Gonçalo Coutinho • StudentId: 11016322' -->
<!-- _class: lead -->

# Stages

    1. Choose dataset;

    2. Unclean the dataset to simulate real life scenarios of messy data;

    3. Identify 3 user stories the dataset should answer;

    4. Proceed with data profiling and build a quality dimensions table;

    5. Clean the data;

    6. Answer the user stories

---

# 1. Dataset

![w:100px][kaggle duck]

Additional columns:

    year = year from the publication_date column
    valid_rating = Boolean value based on text_reviews_count and ratings_count

![h:150 w:1500][dataframe]

---

# 2. Uncleaning

Used python pandas package to transform the dataset.

Created functions to unclean at least 25% of the data.

### Example:

```python
def unclean_title(df):
    sample = select_rows(df)
    return sample.title.str.upper()
```

---

# 3. User Stories

- As a librarian I want to know which are the top rated books by year for the last 10 years so that I can make recommendations to our users.

- As a student I want to know which are the top 10 books and respective authors that have the most text reviews so that I can study what leads to the most user engagement in books.

- As a new fan of Harry Potter I would like to know how many Harry Potter related books exist in english.

---

# 4. Data profiling

![bg right:25% h:150px  w:150px][talend]
![bg right: 25% h:140px  w:140px][mysql]

### Structural analysis:

    1. Connection overview analysis

### Column analysis:

    1. Simple statistics;
    2. Functional dependency analysis;
    3. Nominal analysis;
    4. Pattern frequency analysis;
    5. Discrete data analysis;
    6. Summary statistics analysis

---
<!-- _footer: .-->

## **Quality dimensions table**

![quality dimensions table]

---

# 5. Data Cleaning

![bg right:30% h:720 px  w: px][openrefine]

### Recipe methods used:

- Text transformations
- Regular expression transformations
- Column based transformations
- Clustering
    - nearest neighbor -> levenshtein & ppm
    - key collision -> fingerprint & ngram-fingerprint


---

# 6. Answering the user stories

### 1st user story:

>As a librarian I want to know which are the top rated books by year for the last 10 years so that I can make recommendations to our users.

### Answer:

![top rated books by year]

---

### 2nd user story:

>As a student I want to know which are the top 10 books and respective authors that have the most text reviews so that I can study what leads to the most user engagement in books.

### Answer:

![top text reviewed books]

---

### 3rd user story:

>As a new fan of Harry Potter I would like to know how many Harry Potter related books exist in english.

### Answer:

![harry potter book count]

---

# Thank you! Questions? <!--fit-->
## Github can be found [here][github] and original dataset [here][kaggle]


[//]: # (These are reference links they get stripped out when the markdown processor does its job)
   [github]: <https://github.com/GoncaloCoutinho/Data-Management-Project>
   [kaggle]: <https://www.kaggle.com/jealousleopard/goodreadsbooks>
   [top rated books by year]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a560fe56-324f-4a64-8ac0-e1c9c9a8df93/top_rated_books_by_year.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T182934Z&X-Amz-Expires=86400&X-Amz-Signature=8c4916b7ac598122f95e5d51e8cf905802b77a8575b4a42324db40d4af2f6abb&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22top_rated_books_by_year.png%22&x-id=GetObject
   [top text reviewed books]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3f85fea2-df2c-4791-8024-f5e5ba04e49d/top_text_reviewed_books.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T182931Z&X-Amz-Expires=86400&X-Amz-Signature=000435be5780a38dd6651eaca523206ec6a737fbb44c2578c75940a4047cc0ba&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22top_text_reviewed_books.png%22&x-id=GetObject
   [harry potter book count]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/8750621c-4584-4084-8e68-85c81b2d32d6/how_many_harry_potter_books.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220314T182929Z&X-Amz-Expires=86400&X-Amz-Signature=d2a52d5c5d1ce91627463b08aba99f9623debc868d3a262266f70621c196771b&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22how_many_harry_potter_books.png%22&x-id=GetObject
   [kaggle duck]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/97d4d81f-b955-4fda-8968-18fcbd3c10e8/kaggle_duck.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T123458Z&X-Amz-Expires=86400&X-Amz-Signature=da31769be5f4808e1306a558655ef6e8c8fe5dfc844642e9d08fad27ae4c496c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22kaggle_duck.png%22&x-id=GetObject
   [mysql]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/ab99b483-f5db-4d59-b4d9-cdbe8df274e9/mysql3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T123453Z&X-Amz-Expires=86400&X-Amz-Signature=c06f88ff0a7485d1c210b7ca22251d3b82b320692c631a596469260676cfacf4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22mysql3.png%22&x-id=GetObject
   [openrefine]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/71d70795-3987-4242-b3d0-2245c40c3429/recipe.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T123424Z&X-Amz-Expires=86400&X-Amz-Signature=c3b57b1fcb476af4d16141eb041edcce6a433755fca5bb13a9456cd1d05029bf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22recipe.png%22&x-id=GetObject
   [talend]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cd36659d-0831-4161-b549-5cbb1981f529/talend2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T123448Z&X-Amz-Expires=86400&X-Amz-Signature=d9c684861997882d8e79ed62693dced834d86146a0702ec71fc953fc815db5e5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22talend2.png%22&x-id=GetObject
   [goodreads]:https://s3.us-west-2.amazonaws.com/secure.notion-static.com/baac07f1-97da-4689-b217-9599a4a8364c/goodreads.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T123433Z&X-Amz-Expires=86400&X-Amz-Signature=af17abb8164cdb44c9f308b89a1003043a3fa0f9709df2aeb50494f0d7efd853&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22goodreads.jpg%22&x-id=GetObject
   [dataframe]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/df3fd137-d1ae-4eac-9f52-eb928b4875c3/original_df.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T123429Z&X-Amz-Expires=86400&X-Amz-Signature=267af09ea00f0312fe27329a918849bebc3b8dab687196f048934f09250146c2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22original_df.png%22&x-id=GetObject
   [quality dimensions table]: https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c65e908b-6e67-4f07-8c63-3f13837ec93e/quality_dimensions.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220315T123901Z&X-Amz-Expires=86400&X-Amz-Signature=f5d3b587930000f902a44cf68583e17fae58fef8c89a254918ef2ef69a02c24d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22quality_dimensions.png%22&x-id=GetObject