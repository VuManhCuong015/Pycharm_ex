"""
types of exceptions handling (cac loai xu ly ngoai le)
ZeroDivisionError – Raised when a division by zero is attempted.

IndexError – Occurs when trying to access an invalid index in a list or other sequence.

KeyError – Raised when trying to access a key in a dictionary that does not exist.

TypeError – Occurs when an operation is performed on an inappropriate data type.

ValueError – Raised when a function receives an argument of the right type but an inappropriate value.

OverflowError – Happens when a numerical operation exceeds the memory limit.

FloatingPointError – Related to floating-point arithmetic errors (rare in modern Python).

FileNotFoundError – Raised when trying to open a file that does not exist.

ClassNotFoundError – Not a built-in Python exception, but may be used in some frameworks

MemoryError – Occurs when an operation runs out of memory.
"""
from logging import exception#import 1 ham ten la exception tu python

try:#noi thu nghiem cac doan code co nguy co loi
    user_input = input("Enter a number: ")
    number = int(user_input)#ep kieu chuoi do thanh so nguyen

    result = 100 / number#100 chia cho so vua input
    print(result)

except ValueError:#neu nhap abc hoac 1.5 loi value error
    print("loi roi nhap vao so nguyen ko nhap chu ")

except ZeroDivisionError:#gia su so nguyen 0 hop le nhung / 100 haoc bat ki so nao se loi 
    print("loi khong chia dc 100 cho 0")

except exception as e:#as e dung dat ten bien dai dien cho loi vua xay ra
    print("da xay ra mot loi khac",{e})#in ra noidung loi la gi