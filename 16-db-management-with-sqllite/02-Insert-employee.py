#insert (insert into) them hoac chen du lieu vao bang(table) co san


import sqlite3
#createting database if it already doesn't exist and connect
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

#executing query
cursor.execute('''
INSERT INTO company (name,age,department)
    VALUES (?,?,?)
''', ("Tran Minh Quy",24,"Information technology"))


conn.commit()
conn.close()
print("employee inserted successfully")
