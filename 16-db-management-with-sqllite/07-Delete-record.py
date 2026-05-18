#Delete Record có nghĩa là xóa một hoặc nhiều dòng dữ liệu
# khỏi bảng trong cơ sở dữ liệu.

import sqlite3
#connecting with existing database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

#Get employee id using user input
emp_id = int(input("enter a company id to delete"))


#delete query
cursor.execute("DELETE FROM company WHERE Id = ?", (emp_id, ))

#sau khi xoa hien thi lai toan bo bang ket qua
cursor.execute(("SELECT * FROM company "))
rows = cursor.fetchall()
for row in rows:
    print(row)



#save the changes permanantly by committing
conn.commit()

#print the successful message
print("employee deleted successfully")

#closing the connections
conn.close()

#open db -> nhap id -> xoa dong -> hien thi bang sau khi xoa -> commit -> dong database
