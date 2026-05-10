# Secure Login Application

import bcrypt

# Securely hashed password
stored_password = bcrypt.hashpw(
    b"admin123",
    bcrypt.gensalt()
)

username = input("Enter Username: ")
password = input("Enter Password: ")

# Username validation
if username == "admin":

    # Password verification
    if bcrypt.checkpw(password.encode(), stored_password):
        print("Login Successful")

    else:
        print("Invalid Password")

else:
    print("Invalid Username")
