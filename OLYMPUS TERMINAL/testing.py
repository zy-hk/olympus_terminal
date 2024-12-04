import bcrypt
import csv



# Function to save a new user (username and hashed password) to the CSV file
def save_user(username, password, filename='users.csv'):
    with open(filename, 'a', newline='') as csvfile:  # Append mode to add new users
        writer = csv.writer(csvfile)
        writer.writerow([username, password])
    print(f"User '{username}' saved.")

# Add a user (example usage)
save_user("john_doe", "password123")
save_user("jane_doe", "mysecretpassword")

