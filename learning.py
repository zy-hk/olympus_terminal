import os
import glob

'''
class User:
    def __init__(self, uname, pswrd):
        self.username = uname
        self.password = pswrd

    def display(self):
        print(self.username, self.password)

    def welcome(self):
        print("Hello " + self.username)
'''
passcode = "thisisamystery"
password = "breakfast"


def account_create():
    un = input("Create Username ")
    f = open("users.txt", "a")
    f.write(un + "\n")
    f.close()
    g = open("records.txt", "a")
    g.write("\n")
    g.write("New user registered: " + un + "\n")
    g.close()
    print("You are now registered as a user, " + un)
    print("You currently have access authority: level 1")
    password = "breakfast"
    print("The password is: " + password)
    print("Do not forget it.")
    return un


def sign_in():
    enter_username = input("Input Username: ").strip()
    enter_password = input("Enter Password: ").strip()
    with open("users.txt", "r") as f:
        users = f.read().splitlines()
    if enter_username in users or enter_username == "admin":
        print("username accepted")
        if enter_password == password or enter_password == passcode:
            print("access granted")
            correct = True
            return correct
        else:
            print("incorrect input")
    else:
        print("incorrect input")
        enter_username = input("Input Username: ")
        enter_password = input("Enter Password: ")
    f.close()

def todo(action):
    g = open("records.txt", "a")
    if action == "gotcha":
        print("works!")
        return True
    if action == "leave":
        g.write("\n")
        g.write(username + " left")
        exit()
    if action == "sea":
        folder_path = '/allfiles'
        all_files = glob.glob(os.path.join(folder_path, '*.txt'))
        for file in all_files:
            print(file)
        return True
    if action == "draw":
        old_file = 'allfiles/' + input("OT&/" + username + " !!FILE TO RENAME?!!> ")
        new_file = 'allfiles/' + input("OT&/" + username + " !!NEW NAME (WITH EXTENSION)?!!> ")
        os.rename(old_file, new_file)
        print(f"OT&/" + username + " !!RENAMED {old_file} TO {new_file}!!> ")
        g.write("\n")
        g.write(username + " renamed " + old_file + " to " + new_file)
        return True
    if action == "cook":
        write_file = 'allfiles/' + input("OT&/" + username + " !!FILE TO WRITE TO?!!> ")
        b = open(write_file, "a")
        print("OT&/" + username + " !!WRITE CONTENT BELOW!!> ")
        b.write(input("OT&/" + username + " > "))
        b.close()
        g.write("\n")
        g.write(username + " added to " + write_file)
        return True
    if action == "boom":
        c = open("allfiles/" + username + ".txt", "x")
        print("OT&/" + username + " !!YOU HAVE CREATED " + username + ".txt !!> ")
        c.close()
        g.write("\n")
        g.write(username + " created " + username + ".txt")
        return True
    if action == "shoot":
        die_file = 'allfiles/' + input("OT&/" + username + " !!FILE TO DELETE?!!> ")
        os.remove(die_file)
        print(f"OT&/" + username + " !!{die_file} DELETED!!> ")
        g.write("\n")
        g.write(username + " deleted " + die_file)
        return True
    if action == "hack":
        read_file = 'allfiles/' + input("OT&/" + username + " !!FILE TO READ?!!> ")
        a = open(read_file, "r")
        print(a.read())
        a.close()
        g.write("\n")
        g.write(username + " read " + read_file)
        return True
    if action == "whoami":
        print(username)
        g.write("\n")
        g.write(username + " checked whoami")
        return True
    if action == "padlock":
        print(password)
        g.write("\n")
        g.write(username + " checked padlock")
        return True
    if action == "records":
        h = open("records.txt", "r")
        print(h.read())
        g.write("\n")
        g.write("admin checked records")
        return True
    #UP TO HERE
    g.close()

    

tmpvar = input("Sign in or Create Account? (s/c)")
print("type (e) to leave")

if tmpvar == "c":
    account_create()
    exit()

elif tmpvar == "s":
    correct = sign_in()

elif tmpvar == "e":
    exit()

else: tmpvar = input("Sign in or Create Account? (s/c)")


if correct == True:
    username = input("Please re-enter username: ")
    if username == "admin":
        print("Hello, admin")
        g = open("records.txt", "a")
        g.write("admin" + " logged in")
        g.close()
        f = open("commands.txt", "r")
        print(f.read())
        f.close()
        t = open("admin_co.txt", "r")
        print(t.read())
        t.close()

        for i in range(0,30):
            todo(input("OT&/admin> ")) 
        
    else:
        print("Hello, " + username)
        g = open("records.txt", "a")
        g.write("\n")
        g.write(username + " logged in")
        g.close()
        print("WARNING! You can excecute up to 15 commands before the terminal closes. ")
        f = open("commands.txt", "r")
        print(f.read())
        f.close()

        for i in range(0,15):
            todo(input("OT&/" + username + "> ")) 
    

    


