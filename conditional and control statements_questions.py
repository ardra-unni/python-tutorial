#1. Write a program to check whether a number is positive, negative, or zero.
a=10
if a>0:
    print('a is a positive number')
elif a<0:
    print('a is a negative number')
else:
    print('a is zero')

#output:a is a positive number

#2. Check if a number is even or odd.
a=17
if a%2==0:
    print('a is an even number')
else:
    print("oddd")

#output:oddd

#3. Given a number, check if it is greater than 100.
a=150
if a>100:
    print("a is greater than 100")
else:
    print("a is not greater than 100")

#output:a is greater than 100

#4. Check whether a person is eligible to vote (age  18.
a=20
if a>18:
    print("a is eligible to vote")
else:
    print("a is not eligible to vote")

#output:a is eligible to vote

#5. Given two numbers, print the greater number.
number1=10
number2=20
if number1>number2:
    print(number1)
else:
    print(number2)

#output:20

#6. Given three numbers, print the largest number.
num1=10
num2=25
num3=15
if num1>=num2 and num1>=num3:
    print(num1)
elif num2>=num1 and num2>=num3:
    print(num2)
else:
    print(num3)

#output:25

#7. Check whether a year is a leap year.
a=2024
if a%4==0:
    print("Leap year")
else:
    print("Not a leap year")

#output:leap year

#8. Given a mark, print:
#  "Pass" if marks  40 
#  "Fail" otherwise
a=50
if a>=40:
    print("Pass")
else:
    print("Fail")

#output:pass

#9. Given a mark, print grades:
#  A →  90
#  B →  75
#  C →  60
#  Fail → below 60
a=85
if a>=90:
    print("A")
elif a>=75:
    print("B")
elif a>=60:
    print("C")
else:
    print("Fail")

#output:B

#10. Check if a character is a vowel or consonant.
i="a"
if i in "aeiou":
    print("Vowel")
else:
    print("Consonant")

#output:vowel

#11. Print numbers from 1 to 10 but stop when number is 6.
for a in range(1,11):
    if a==6:
        break
    print(a)

#output:1 2 3 4 5

#12. Print numbers from 1 to 10 but skip number 5.
for a in range(1,11):
    if a==5:
        continue
    print(a)

#output:1 2 3 4 6 7 8 9 10

#13. Use pass inside an if block and explain why it doesnʼt cause an error.
a=1
if a>0:
    pass
else:
    print("Negative or zero")

# pass means do nothing.it is used when we need an empty block.

#14. Print all even numbers between 1 and 20.
for a in range(1, 21):
    if a%2==0:
        print(a)

#output:2 4 6 8 10 12 14 16 18 20

#15. Find the sum of numbers from 1 to 10. 
sum=0
for a in range(1,11):
    sum=sum+a
print(sum)

#output:55

#16. Check whether a given number is a multiple of both 3 and 5.
a=15
if a%3==0 and a%5==0:
    print("Multiple of both 3 and 5")
else:
    print("Not a multiple of both")

#output:multiplt of both 3 and 5

#17. Print "Hello" 5 times using a loop.
for a in range(5):
    print("Hello")

#output:Hello Hello Hello Hello Hello

#18. Given a list 1,2,3,4,5 , print only numbers greater than 3.
numbers=[1,2,3,4,5]
for a in numbers:
    if a>3:
        print(a)

#output:4 5

#19. Advanced Login System
#  Write a Python program to simulate a login system with the following rules:
#a.  The correct username is "admin" and the correct password is "1234" .
#b.  The user is allowed a maximum of 3 login atte
#c.  The username comparison should be case-insensitive.

#d.  The password comparison should be case-sensitive.
#e.  If the user enters correct credentials within the allowed attempts, display
#     Login successful .
#f.  If all attempts are used without success, display
#     Account locked .
#g.  After each failed attempt, display the number of attempts remaining.
correct_username = "admin"
correct_password = "1234"
for i in range(3):
    username = input("enter the username: ")
    password = input("enter password: ")
    if username=="admin" and password=="1234":
        print("Login successful")
        break
    else:
        print("Attempts remaining:", 2 - i)

else:
    print("Account locked")

#output:enter username:admin enter password:1234 login successful

#20. Enhanced Traffic Light Controller
#  Write a Python program that acts as a traffic light controller with the following conditions:
#  The program should accept either a color or a number as input.
#  Use the mapping:
#  1 or "red"  Stop and wait for 60 seconds
#  2 or "yellow"  Ready and wait for 5 seconds
#  3 or "green"  Go and drive safely
#  The program should handle inputs in a case-insensitive manner.
#  If the input does not match any valid color or number, display
#     Invalid signal.
signal = "yellow"
if signal.lower() == "red" or signal == "1":
    print("Stop and wait for 60 seconds")
elif signal.lower() == "yellow" or signal == "2":
    print("Ready and wait for 5 seconds")
elif signal.lower() == "green" or signal == "3":
    print("Go and drive safely")
else:
    print("Invalid signal")

#output:ready and waiting for 5 seconds

#LIST COMPREHENSION QUESTIONS
#   Given a list of numbers, write a program to find the sum of all numbers, the sum of even numbers, and the sum of odd numbers using list comprehension.
numbers = [1, 2, 3, 4, 5]
all_sum = sum([a for a in numbers])
even_sum = sum([a for a in numbers if a % 2 == 0])
odd_sum = sum([a for a in numbers if a % 2 != 0])

print("Sum of all numbers:", all_sum)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#output:Sum of all numbers: 15 Sum of even numbers: 6 Sum of odd numbers: 9

#   Given a list of numbers, create a new list that contains only numbers greater than 10 and divisible by 3 using list comprehension.
numbers = [3, 6, 12, 15, 20, 24]
result =[ x for x in numbers if x > 10 and x % 3 == 0]

print(result)

#output:[12, 15, 24]

#   Given a list of numbers, create a new list containing only even numbers greater than 10 using list comprehension.
numbers = [5, 10, 12, 15, 18, 20]
result = [x for x in numbers if x > 10 and x % 2 == 0]

print(result)

#output:[12, 18, 20]

#   Given a list of strings, create a new list containing the length of each string using list comprehension.
a = ["apple", "banana", "cat"]
result = [len(a) for word in a]

print(result)

#putput:[5, 6, 3]

#   Given a list of numbers, create a new list where:
#  even numbers are replaced with "even"
#  odd numbers are replaced with "odd"
numbers = [1, 2, 3, 4, 5]
result = ["even" if x % 2 == 0 else "odd" for x in numbers]

print(result)

#output:['odd', 'even', 'odd', 'even', 'odd']