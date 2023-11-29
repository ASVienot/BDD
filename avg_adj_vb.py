# Nombre moyen des adjectifs pour les reviews d'un nombre d'etoiles donné par l'utilisateur.

import sqlite3
import spacy

nlp = spacy.load("en_core_web_sm")

# Call sqlite3.connect() to create a connection to the database projet_bdd.db in the current working directory
# In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. 
# Call con.cursor() to create the Cursor

con = sqlite3.connect("projet_bdd.db")
cur = con.cursor()


rating = int(input("Nombre d'étoiles des commentaires que vous voulez analyser: "))

query_params = (rating, )

result = cur.execute("""SELECT review FROM reviews
                     WHERE review_scores_rating = ?""", query_params)

rows = result.fetchall()


#result.fetchall() to get all the results of the query
#print(result.fetchone())

def get_average_pos(rows):
    if len(rows) == 0:
        return 0.0, 0.0
    adj, verb = 0, 0
    for row in rows:
        text = row[0]
        doc = nlp(text)   
        for token in doc:
            # Get the token text, part-of-speech tag and dependency label
            #token_text = token.text
            token_pos = token.pos_
            if token_pos == "ADJ":
                adj = adj + 1
            elif token_pos == "VERB" or token_pos == "AUX":
                verb = verb + 1
            #token_dep = token.dep_
            # This is for formatting only
            #print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")
    average_adj = adj / len(rows)
    average_verb = verb / len(rows)
    return average_adj, average_verb

average_adj, average_verb = get_average_pos(rows)
print(f"Il y a une moyenne de {average_adj:.3} adjectifs et {average_verb:.3} verbes dans les commentaires avec un score général de {rating} étoiles")


