#queue firt in firt out vao truoc lay ra truoc
list1 = []#chua cac phan tu cua stack
while True:#tao 1 vong lap vo han de chuong trinh chay cho den lenh break
    oprInput = int(input('''opr=operator toan tu 
    1.push element (them vao)
    2.pop first element (lay ra dau tien)
    3.front element (lon nhat)
    4.rear element (hien thi)
    5.display queue (thoat chuong trinh)
    6.exit 
    '''))
    if oprInput == 1:
        userinput = input("enter a value:")
        list1.append(userinput)
        print(list1)
    elif oprInput == 2:
        if len(list1) == 0:
            print("empty queue")
        else:
            del list1[0]
            print(list1)
    elif oprInput == 3:
        if len(list1) == 0:
            print("empty queue")
        else:
            print("firts element of queue is:", list1[0])
    elif oprInput == 4:
        if len(list1) == 0:
            print("empty queue")
        else:
            print("last queue element:", list1[-1])
    if oprInput == 5:
        print(list1)
    elif oprInput == 6:
        break
    else:
        print("invalid Operation")