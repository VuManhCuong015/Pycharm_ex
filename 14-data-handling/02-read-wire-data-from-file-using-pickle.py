#write and read data into files
import pickle


# data = {
#     "name":"Cuong",
#     "age":20,
#     "profession":"intern",
#     "salary":"0$",
# }
# writeData = open ("my-data-txt", "wb")#tao file ghi,wb
# pickle.dump(data, writeData)#dong goi du lieu vao file,wb ghi duoi dang nhi phan
# writeData.close()#dong file



# Read Data from a file
myFile = open("my-data-txt", "rb")
loadData = pickle.load(myFile)
print(loadData)