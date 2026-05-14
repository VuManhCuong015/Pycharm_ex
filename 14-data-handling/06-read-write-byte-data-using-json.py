import json
#define a json data
data = {
    "name":"Cuong",
    "age":21,
    "skills":"python"
}
print(type(data))
jsonString = json.dumps(data,indent=4)#dums(dump string) lay dict ep no thanh dang stirng

#convert python object into json string
#indent 4 tu dong them khoang trang trinh bay dep hon
#print(type(jsonString))#kiem tra loai cua bien moi

# print("json string:", jsonString)
# convert json string back into python object
pythonObject = json.loads(jsonString)
print(type(pythonObject))
print("python object",pythonObject)