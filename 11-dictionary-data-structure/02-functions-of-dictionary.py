#dictionary python cung cap nhieu ham(functions)

#cac functions co ban
#len(dict)tra ve so luong cap KEY-VALUE
#type(dict)xac nhan kieu du lieu se tra ve
#dict() khoi tao mot dictionary moi

#cac phuong thuc truy xuat du lieu
#.keys():tra ve danh sach cac khoa
#.values():tra ve danh sach cac gia tri
#.items():tra ve danh sach cho cac cap KEY-VALUE
#.get(key, default): tra ve gia tri cua mot khoa neu kha do ko ton tai tra ve None

#cac phuong thuc chinh sua dict
#.update({key: value}) update dict moi voi KEY_VALUE tu mot dict khac
#.pop(key) xoa KEY duoc chon va tra ve VALUE cua no
#.popitem() xoa va tra ve KEY-VALUE cuoi cung duoc them vao
#.clear() xoa KEY-VALUE trong dict

dictionary = {
    'name':'vu manh cuong',
    'age':20,
    'asset':'poor'
}
# for i in dictionary.keys():#vong lap for i dong vai tro nhu mot bien lap
#     print(i)
#
# for v in dictionary.values():
#     print(v)
#
# for k, v in dictionary.items():
#     print(k,v)
# print(dictionary['name'])
# print(dictionary.get('name'))#dung get neu key khong ton tai no se tra ve none ma khong bao loi

#print(dictionary)
# #del dictionary['name']
# dictionary.pop('name')
# print(dictionary)

d2 = dict(name = 'manh cuong', age = 20, asset = 'poor')
print(d2)
d2.update({'name':'vu manh cuong'})
d2['age'] = 30
print(d2)
d2.clear()
print(d2)