import sqlite3

#connect database and create a database if it not already exist

conn = sqlite3.connect("company.db")#ra lenh cho python ket noi toi file csdl co ten la company.db
# print("Database connected successfully")


#create a cursor to execute sql commands
cursor = conn.cursor()#tao ramot doi tuong goi la cursor
# CREATE TABLE IF NOT EXISTS company: Tạo một cái bảng (Sheet) tên là company nếu như bảng này chưa tồn tại.
#
# id INTEGER PRIMARY KEY AUTOINCREMENT: Tạo cột id chứa số nguyên, làm khóa chính (không được trùng lặp) và tự động tăng số (1, 2, 3...) mỗi khi có nhân viên mới mà không cần bạn phải tự nhập.
#
# name TEXT NOT NULL: Tạo cột name chứa văn bản (tên nhân viên) và bắt buộc phải nhập, không được để trống (NOT NULL).
#
# age INTEGER: Tạo cột age chứa số nguyên để lưu tuổi.
#
# department TEXT: Tạo cột department chứa văn bản để lưu tên phòng ban.
cursor.execute('''
CREATE TABLE IF NOT EXISTS company(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
''')

conn.commit()
conn.close()
print("Table created successfully and connection closed")
