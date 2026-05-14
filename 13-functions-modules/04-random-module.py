#randint va randrange deu thuoc thu vien random va duoc dung de tao so nguyen ngau nhien
#randint la tra ve mot so nguyen ngau nhien nam trong khoang tu a den b
#example:random.randint(start,stop)
#randrange(start,stop,step
import random
list1 = [3,9,40,30,23,11]
print("randint", random.randint(1,10))
print("randrange", random.randrange(1,10))
print("Choice",random.choice(list1))#ham choice se boc ngau nhien mot phan tu duy nhat tu list1
print("random", random.random())#khong co tham so ben trong ngoac thi ket qua random se tra ve so thap phan tu 0.0->1 nhuwng khong baoh dat chinh xac la 1

#print ("Shuffle",random.shuffle(list1))
#ham shuffle chay ra none vi ham tra ve gia tri randint hay choice da tinh toan xong va duwa ra ket qua ban in ra
#ham shuffle thuoc nhom nay nhiem vu cua no nhay vao danhs ach rong de xao tron cac phan tu trong do
#nen -> khi do ham shuffle se tra ve none


random.shuffle(list1)
print("shuffle", list1)
print("Uniform", random.uniform(1,10))#ham uniform lay so thap phan ngau nhien tu 1 den 10
