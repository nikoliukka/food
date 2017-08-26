from Dinner import Dinner

import sqlite3

connection = sqlite3.connect("lite.db")

dinner = Dinner(connection)

while (True):
    action = input("Syötä uusi ruoka tai jätä tyhjäksi saadaksesi ehdotus: ")

    if (action == "-1"):
        break
    elif (len(action) > 0):
        dinner.insert(action)
    else:
        print (dinner.getRandom())

connection.close
