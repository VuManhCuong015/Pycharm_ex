# #example 1
# num1 = 10
# num2 = 0
#
# try:
#     result = num1 / num2
# except ZeroDivisionError:
#     print ("dontt divide it by zero,try again")
# else:
#     print (result)
# finally:
#     print("execution completed")

#example 2
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))

try:
    result = num1 / num2
#except (TypeError , ZeroDivisionError) as e:
except Exception as e:
    print (f"an error occurred{e}",)
else:
    print (result)
finally:
    print("execution completed")

