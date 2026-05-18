#Join là cách kết hợp dữ liệu từ 2 bảng
# trở lên thành một kết quả duy nhất, dựa trên một cột chung giữa chúng.
#join co 4 kieu thuong dung nhieu
#INNER JOIN (Lấy phần giao nhau - Mặc định)
#LEFT JOIN (Lấy hết sạch bảng bên trái)
#JOIN kết hợp điều kiện lọc (WHERE)
#JOIN kết hợp sắp xếp dữ liệu (ORDER BY)

import sqlite3
#connecting with existing database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

#create project table
cursor.execute('''
 CREATE TABLE IF NOT EXISTS project(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
     emp_id INTEGER,
     project_name TEXT,
     FOREIGN KEY (emp_id) REFERENCES company (id)
 )
''')

#insert project data
#cursor.execute("INSERT INTO project(emp_id, project_name) VALUES(?,?)",(9,"Information technology"))
# print("New record has been added successfully")

#joining tables and fetching combined data
cursor.execute('''
    SELECT company.name, company.age,project.project_name FROM company LEFT JOIN project ON company.id = project.emp_id
        
''')
rows = cursor.fetchall()
#loop through all records
for row in rows:
    print(row)


#saving the changes
conn.commit()
#closing the connection
conn.close()