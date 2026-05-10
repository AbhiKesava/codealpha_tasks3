# Vulnerable Login Application

username = input("Enter Username: ")
password = input("Enter Password: ")

# Hardcoded credentials
if username == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Invalid Credentials")
