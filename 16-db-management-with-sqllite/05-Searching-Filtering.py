#SEARCHING (Tìm kiếm) cursor.execute("SELECT * FROM company WHERE name = 'Cuong'")
#và FILTERING (Lọc).
import sqlite3
#connecting with existing database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

#get input from user
dept = input("enter department to search employee:")
#filter by age
#cursor.execute("SELECT * FROM company WHERE age > 21")

# cursor.execute("SELECT * FROM company WHERE department = ?",(dept,))
cursor.execute("SELECT * FROM company WHERE department LIKE ?",('%' + dept+ '%',))
#% dung de tim kiem gan dung vi du bo thi ra boss

rows = cursor.fetchall()

#loop through all records
for row in rows:
    print(row)

conn.close()