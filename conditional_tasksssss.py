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