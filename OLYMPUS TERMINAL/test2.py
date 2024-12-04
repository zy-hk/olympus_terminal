import bcrypt
import csv

# Function to load users from the CSV file
def load_users(filename='users.csv'):
    users = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Ensure it's not an empty row
                users[row[0]] = row[1]  # username: hashed_password
    return users

# Function to verify username and password
def verify_user(username, password, filename='users.csv'):
    users = load_users(filename)
    if username in users:
        password_saved = users[username]
        if password_saved == password:
            print("Access granted.")
            return True
        else:
            print("Invalid password.")
    else:
        print("User not found.")
    return False

username1 = input("what is? ")
password1 = input("what is? ")

if verify_user(username1, password1):
    print("Login successful")
else:
    print("Login failed")