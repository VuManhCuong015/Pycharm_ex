#display record hay la VIEW/SELECT RECORD hien thi hoac lay ra xem cac dong du lieu dang luu tru ben trong bang
import sqlite3
#connectin with existing database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

#fetch records query
cursor.execute("""SELECT * FROM company """)
rows = cursor.fetchall()#fetch lay di mang ve ham nay ra lenh cho con tro be toan bo du lieu da dc select
#rows tao mot bien rows(cac dong) de hung toan bo du lieu ma fetcall mang ve

for row in rows:
    # print("company name", row[1])#moi danh sach du lieu deu duoc dem stt bat dau tu 0 nen khi ta chon 0 thi no se lay

    # ra id chon 1 se
    #lay ra name
    print(row)
conn.close()#dong ket noi voi file company.db