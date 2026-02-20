# login_system.py

# Stored correct credentials
correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ").lower()
password = input("Enter password: ")

if username == correct_username.lower():
    if password == correct_password:
        print("Welcome! Login successful.")
    else:
        print("Incorrect password.")
else:
    print("User not found.")

