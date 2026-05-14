val1 = eval(input("enter a first number:"))
val2 = eval(input("enter a second number"))
oper = input("enter operator:")
if oper == "+":
    print (val1 + val2)
elif oper == "-":
    print(val1 - val2)
elif oper == "*":
    print(val1 * val2)
elif oper == "/":
    print(val1 / val2)
else:
    print("Operation not invalid")