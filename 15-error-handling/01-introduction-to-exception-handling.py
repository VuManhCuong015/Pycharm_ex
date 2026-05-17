"""
An exception in Python is an event that occurs during program
execution and disrupts the normal flow of the program.
It usually happens when an error occurs, such as dividing by zero,
accessing an invalid index, or trying to open a non-existent file.

Exception handling is a mechanism in Python that allows us
to handle runtime errors gracefully instead of crashing the program
"""
#vi du code
#cach xu ly bang exception handling
#co che hoat dong cua try except la den dong 16 cos loi python se dung khoi try tai day
#va dong print result se bi block ko dc chay
#sau do python nhay xuong dong except de xu ly loi va in ra
#sau do code ko loi va tiep tuc chay toi dong cuoi cung
try:#gia su code co nguy co loi
    numerator = 10
    demoninator = 0
    result = numerator / demoninator #viec 1 so chia cho 0 la no hop le
    print (result)
except ZeroDivisionError:#code nay se chay neu khoi try xay ra loi
    print ("xay ra loi khong chia dc mot so cho 0")

print ("chuong trinh van hoat dong bthg")


