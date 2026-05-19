#cac chuc nang cua mini project
#add new employee (them nhan vien)
#view all employ (hien thi dnah sach)
#search by department (tim kiem theo phong)
#update employee(cap nhat thong tin)
#delete employee (xoa nhan vien)
#assign project to employee (phan cong duan)
#view employee with project (xem nv cung duan cua ho)


import sqlite3

def get_connection():
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()
    return conn, cursor

def create_tables():
    conn, cursor = get_connection()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS project(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_id INTEGER,
        project_name TEXT,
        FOREIGN KEY (emp_id) REFERENCES company (id)
    )
    ''')


    conn.commit()
    conn.close()

def add_employee():
    name = input("Enter employee name:")
    age = int(input("Enter employee age:"))
    dept = input("Enter department:")

    conn, cursor = get_connection()
    cursor.execute("INSERT INTO company(name,age,department) VALUES (?,?,?)", (name,age,dept))

    conn.commit()#luu thay doi vao file db
    conn.close()#dong ket noi
    print("employee added successfully")

def view_employees():
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM company")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("")

def search_by_department():
    dept = input("Enter department to search:")
    conn, cursor = get_connection()
    cursor.execute("SELECT * FROM company WHERE department = ?", (dept,))


    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("")

def  update_employee():
    emp_id = int(input("Enter employee id to update:"))
    new_dept = input("Enter new department")
    conn, cursor = get_connection()
    cursor.execute("UPDATE company SET department = ? WHERE id = ?", (new_dept, emp_id))

    conn.commit()
    conn.close()
    print("employee updated successfully")

def  delete_employee():
    emp_id = int(input("Enter employee id to delete:"))
    conn, cursor = get_connection()
    cursor.execute("DELETE FROM company WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()
    print("employee delete successfully")

def  assign_project():
    emp_id = int(input("Enter employee id:"))
    project_name = input("Enter project name:")
    conn, cursor = get_connection()
    cursor.execute("INSERT INTO project (emp_id, project_name) VALUES (?, ?)",(emp_id, project_name))
    conn.commit()
    conn.close()
    print("project assign successfully")

def  view_employee_with_project ():
    conn, cursor = get_connection()
    cursor.execute('''
        SELECT company.name, company.department, project.project_name
        FROM company 
        INNER JOIN project ON company.id = project.emp_id
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
    print("")

def menu():
    create_tables()
    while True:
        print("===Employee Management System===")
        print("1. add employee")
        print("2. View all employees")
        print("3. search by department")
        print("4.update employee details")
        print("5.delete employee")
        print("6.assign project to employee")
        print("7.view employee with project")
        print("0.exit program")

        choice = input("Enter your choice:")
        print()

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_by_department()
        elif choice == '4':
            view_employee_with_project()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            assign_project()
        elif choice == '7':
            view_employee_with_project()
        elif choice == '0':
            print("program is exiting")
            break
        else:
            print("invalid choice,try again\n")

if __name__ == '__main__':#neu file nay duoc chay truc tiep hay kich hoat ham main bam run file la menu hien ra de dung
#import file nay sang file khac de menu khong tu dong nhay lung tung
    menu()
