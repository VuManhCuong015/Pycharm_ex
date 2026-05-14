""""
rong Python, JSON module là một thư viện tích hợp sẵn dùng để làm việc
với dữ liệu định dạng JSON (JavaScript Object Notation).

Tương tự như pickle, module json cũng có
4 hàm chính với quy tắc đặt tên y hệt (chữ s dành cho chuỗi/biến):

Ghi dữ liệu (Python → JSON) voi file
json.dump(obj, file)
Ghi dữ liệu (Python → JSON) voi string
json.dumps(obj)
Đọc dữ liệu (JSON → Python) voi file
json.load(file)
Đọc dữ liệu (JSON → Python)
json.loads(string)
"""

import json
people = {
    "name":"Cuong",
    "age":21,
    "skills":"python",
}

#dict-> Json(serialization)
json_string = json.dumps(people)
print(json_string)

#doc tu file.json
with open("people.json", "w") as file:
    json.dump(people, file)
    print(people)