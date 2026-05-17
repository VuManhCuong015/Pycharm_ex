#ordering and limit sap xep va gioi han
#order bt sap xep theo thu tu mong muon
#asc(ascending) tu nho den lon
#desc(descending) tu lon den nho
#limit gioi han so luong
import sqlite3

#connecting with existing database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

#sort records with order by
cursor.execute("""SELECT * FROM company ORDER BY age ASC LIMIT 2 """)
rows = cursor.fetchall()

#loop through all company
for row in rows:
    print(row)


conn.close()