#error and exception handling in python
#1 errors in python

#2 common python errors
#zero division error

#a=10
#b=0
#print(a/b)

#type error

#a="hello"
#b=5
#print(a+b)

#value error

#a=int("hello")
#print(a)

#index error

#a=[10,20,30]
#print(a[5])

#key error

#a={"name":"ardra"}
#print(a["age"])

#file not found error

#file= open("data.txt")

#3 try-except
try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("can't devide by zero")

#4 using else and finally in exception handling
#else block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("The result is", result)

#finally block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always be printed.")