#set la tap hop cau truc dung luu tru phan tu
#(unique)set khong cho phep ta nhap cac phan tu trung lap
#(unordered)cac phan tu khong co vi tri co dinh nen ta khong the dung set[0] de lay phan tu dau tien
#(unchangeable)khong the sua mot phan tu vd 5 -> 10 nhung ban co the them moi hoac xoa bo chung
#cu phap cua set su dung {} giong dict nhung khong co KEY-VALUE chi co gia tri don le
#vidu: set1 = {1,2,3,4,5,6,7,8,9,10}

set1 = {10,20,90,200,100,10}
# print(set1)

# for i in set1:
#     print(i)

print(set1)
# set1.discard(11)#neu 11 khong ton tai trong set thi python se khong lam gi van chay bthg
# set1.remove(200)#neu phan tu x khong ton tai trong set python se bao loi ngay lap tuc
# set1.pop()#xoa mot phan tu ngau nhien khoi pop
# set1.clear()#xoa toan bo set
# set1.add(35)
list1 = [10,25,55,32]
set1.update(list1)
print(set1)#print set1 sau khi xoa 200