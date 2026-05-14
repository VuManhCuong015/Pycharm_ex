#stack la cau truc du lieu hoat dong lifo (lasst in first ouut)
list1 = []#chua cac phan tu cua stack
while True:#tao 1 vong lap vo han de chuong trinh chay cho den lenh break
    oprInput = int(input('''opr=operator toan tu 
    1.push element (them vao)
    2.pop element (lay ra)
    3.peek element (lon nhat)
    4.display element (hien thi)
    5.exit element (thoat chuong trinh)
    '''))
    if oprInput == 1:
        userinput = input("enter a value:")
        list1.append(userinput)
        print(list1)
    elif oprInput == 2:
        if len(list1) == 0:
            print("empty stack")
        else:
            popElement = list1.pop()
            print("pop element:",popElement)
            print(list1)
    elif oprInput == 3:
        if len(list1) == 0:
            print("empty stack")
        else:
            print("last element of stack is:",list1[-1])
    elif oprInput == 4:
        print("display stack:", list1)
    if oprInput == 5:
        break;
    else:
        print("invalid Operation")