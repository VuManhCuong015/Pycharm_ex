# userInput = input("enter the string")
# print(userInput)
# list1 = userInput.split()#split de tach rieng cac chu ra
# print(list1)
list1 = []#khoi tao list 1 rong chua cac ky  tu nhap vao
for i in range(1, 5):#vong lap 4 lan bien i nhan gia tri
    userInput = input("enter a string"+ str(i)+": ")
    list1.append(userInput)
    print(userInput)
print(list1)
