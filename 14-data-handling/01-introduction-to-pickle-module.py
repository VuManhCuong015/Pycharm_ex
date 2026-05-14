#pickling: la qu tỉnh chuyen doi mot doi tuong python
#ex mot danh sach ten khach hang thanh mot dong du lieu nhi phan byte stream
#unpickling la qua trinh nguoc lai chuyen dong du lieu nhi phan do tro lai thanh doi tuong python ban dau voi day du thuoc tinh va du lieu
#dung pickle la vi trong luc lam viec muon safe du lieu tho nhu txt hay csv
#ma muon luu trang thai cua mot doi tuong phuc tap

#de dung pickle ta can import pickle
#pickle co hai cap ham chinh
#hamf dung cho file de luu du lieu pickle.dump(obj, file)
#___________________de doc du lieu pickle.load(file)

#ham dung cho bien (chuoi byte)
#ham dung cho file de luu du lieu pickle.dump(obj)
#ham dung cho file de doc du lieu pickle.loads(bytes_obj)

import pickle
data = {"name":"manh cuong","age":30, "sex":"male"}

#pickle luu vao file nhi phan (wb = write binary)
with open("data.pickle","wb") as f:
    pickle.dump(data,f)

#unpicking doc tu file (rb = read binary)
with open("data.pickle","rb") as f:
    data = pickle.load(f)

print(data)