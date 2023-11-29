import sqlite3
from textblob import TextBlob
from tabulate import tabulate


con = sqlite3.connect("projet_bdd.db")
cur = con.cursor()

# Call sqlite3.connect() to create a connection to the database projet_bdd.db in the current working directory
# In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. 
# Call con.cursor() to create the Cursor

result = cur.execute("""SELECT review, review_scores_cleanliness, review_scores_rating FROM reviews
                     WHERE review LIKE "%clean%" 
                     ORDER BY "review_scores_cleanliness" """)


#review that has clean, cleanliness score, overall score
table_data = []
for row in result:
    blob = TextBlob(row[0])
    row_data = [row[0], row[1], row[2], blob.sentiment.polarity]
    table_data.append(row_data)
    
print(tabulate(table_data, headers=["Review", "Cleanliness score", "Overall score", "Review polarity"], tablefmt="grid", maxcolwidths=80))

