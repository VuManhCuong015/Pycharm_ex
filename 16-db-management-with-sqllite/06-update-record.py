#Trong database, "update record" nghĩa là sửa đổi hoặc cập nhật dữ liệu
# của một (hoặc nhiều) dòng đã có sẵn trong bảng.

import sqlite3
#connecting with existing database
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

#get company id from user
emp_id = int(input("enter a company id to update"))

#get department from company to update it
new_dept = input("enter new department name")

#sqlite query to update the company record
cursor.execute("UPDATE company set department = ? WHERE id = ?", (new_dept, emp_id))

#commit the changes
conn.commit()

#printing a successful message
print("company updated successfully")

#close the connections
conn.close()
