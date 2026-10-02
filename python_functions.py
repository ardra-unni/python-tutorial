def greet():# function
    print()

# function call
greet()

# function definition
def greet(name,age,place): #parameters : variables listed inside the parenthesis
    print(f"hello {name} your age is {age} and your place is {place}")

# function call
greet("ardra",21,"pandikkad") # arguments : values passed inside the parenthesis


# type of arguments
# positional arguments
def greet(name,age,place):
    print(f"hello {name} your age is {age} and your place is {place}")

greet("ardra",21,"pandikkad")

# keyword arguments
def greet(name,age,place):
    print(f"hello {name} your age is {age} and your place is {place}")

greet(age=21,name="ardra",place="pandikkad")

# defult arguments
def greet(name,age,place="no place selected"):
    print(f"hello {name} your age is {age} and your place is {place}")

greet("ardra",21)

# arbitrary arguments
def numbers(*a):
    print(a)

numbers(1,2,3,4,5,6,7,8,9,10)

# arbitrary keyword arguments
def details(**a):
    print(a)

details(name="ardra",age=21,place="pandikkad")

def details(name,*arguments,**keywordarguments):
    print(name)
    print(arguments)
    print(keywordarguments)

details("ardra",1,2,3,4,5,6,7,8,9,10,fname="ardra",age=21,place="pandikkad")

# for loop
n=10
sum=0
for i in range(1,n+1):
     sum+=i # sum=sum+i

print(sum)

#while loop
n=15
sum=0
i=1
while i<=n:
   sum+=i
   i+=1
print(sum)

#local variable
def test():
    a=10
    print(a)
test()

#global variable
a=10
def test():
    print(a)
test()

#return statement
def sum(a,b):
    print(a)
    print(b)
    return a+b
print(sum(7,5))

#lambda function
def greet(name):
    return f"hello,{name}!"

print(greet("alice"))

a=lambda name:f"hello,{name}!"
print(a("alice")) 

#def add(a,b):
#    return a+b
#print(add(3,4))

a=lambda a,b: a+b
print(a(3,4))

a=0
if a>0:
    print('a is a positive number')
elif a<0:
    print('a is a negative number')
else:
    print('a is zero')

def greet(a):
    if a>0:
     print('a is a positive number')
    elif a<0:
     print('a is a negative number')
    else:
     print('a is zero')

greet(1)
greet(-1)
greet(0)

#odd and even
def greet(a):

    if a %2==0:
        print('a is an even number')
    else:
        print("oddd")

greet(0)
greet(2)

# largest among three numbers
def add(a,b,c):
   
    if a>b and a>c:
        print('a is greater')
    elif b>a and b>c:
        print('b is greater')
    else :
        print('c is greater')

add(5,7,3)

def greet(name):
    print(len(name))

greet("ardra")

def greet(name):
    print(name.upper())

greet("ardra")


