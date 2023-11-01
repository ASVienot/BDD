import sqlite3
import spacy

nlp = spacy.load("en_core_web_sm")

# Call sqlite3.connect() to create a connection to the database projet_bdd.db in the current working directory
con = sqlite3.connect("projet_bdd.db")

# In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. 
# Call con.cursor() to create the Cursor
cur = con.cursor()
result = cur.execute("""SELECT review FROM reviews
                     WHERE review_scores_rating = 5""")

#result.fetchall() to get all the results of the query
#print(result.fetchone())

rows = result.fetchall()

n = 0
for row in rows:
    text = row[0]
    # Process the text
    doc = nlp(text)   
    for token in doc:
        # Get the token text, part-of-speech tag and dependency label
        token_text = token.text
        token_pos = token.pos_
        if token_pos == "ADJ":
            n = n + 1
        token_dep = token.dep_
        # This is for formatting only
        #print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

average_adj = n/len(rows)
print(f"There is an average of {average_adj:.3} adjectives in the reviews with a general score of 5")

