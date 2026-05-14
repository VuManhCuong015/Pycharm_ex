students = {
    'cuong':{'age':20, 'education':'Dai Nam University', 'semster':'second years'},
    'khanh': {'age': 21, 'education': 'back khoa University', 'semster': 'third years'},
    'vu': {'age': 23, 'education': 'ngoai thuong University', 'semster': 'final years'},
    'tuan': {'age': 24, 'education': 'kinh te quoc dan University', 'semster': 'second years'},
}
#print(student)
# for k,v in student.items():
#     print(k,v['age'], v['education'])

# for k,v in students.items():
#     print(k,v)

students['cuong']['age'] = 21
for k,v in students.items():
    print(k,v)


