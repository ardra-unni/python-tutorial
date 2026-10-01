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