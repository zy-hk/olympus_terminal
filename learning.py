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
password = "lunch:)hour"


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
    password = "lunch:)hour"
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
        g.write("\n")
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
        print(f"OT&/" + username + " !!RENAMED " + old_file + " TO " + new_file + "!!> ")
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
    if action == "board":
        bo = open("board.txt", "r")
        print(bo.read())
        bo.close()
        g.write("\n")
        g.write(username + "checked the public board")
        return True
    if action == "records":
        h = open("records.txt", "r")
        print(h.read())
        h.close()
        g.write("\n")
        g.write("admin checked records")
        return True
    if action == "users":
        u = open("users.txt", "r")
        print(u.read())
        u.close()
        g.write("\n")
        g.write("admin checked users.txt")
        return True
    if action == "views":
        v = open("admin.txt", "r")
        print(v.read())
        v.close()
        g.write("\n")
        g.write("admin checked admin.txt")
        return True
    if action == "level2":
        lt = open("level2.txt", "r")
        print(lt.read())
        lt.close()
        g.write("\n")
        g.write("admin checked level2.txt")
        return True
    if action == "inbox":
        ib = open("admin_email.txt", "r")
        print(ib.read())
        ib.close()
        g.write("\n")
        g.write("admin checked admin email")
        return True
    if action == "second":
        at = open("level2.txt", "a")
        print("please type username to increase access")
        at.write("\n")
        newname = input("OT&/admin> ")
        at.write(newname)
        at.close()
        g.write("\n")
        g.write("admin increased " + newname + " to level 2 access")
        return True
    if action == "post":
        bo = open("board.txt", "a")
        bo.write("--------------------------------------------------------------------------------------------")
        bo.write("\n")
        bo.write("Post by " + username + " : " + input("OT&/" + username + " !!POST TITLE?!> "))
        bo.write("\n")
        print("OT&/" + username + " !!WRITE POST CONTENT BELOW!!> ")
        bo.write("\n")
        bo.write(input("OT&/" + username + " > "))
        bo.write("\n")
        bo.write("--------------------------------------------------------------------------------------------")
        bo.write("\n")
        bo.close()
        print("OT&/" + username + " !!POSTED!!> ")
        g.write("\n")
        g.write(username + " added a post to public board.")
    if action == "email":
        ae = open("admin_email.txt", "a")
        ae.write("\n")
        ae.write("Message from  " + username)
        ae.write("\n")
        print("OT&/" + username + " !!WRITE MESSAGE BELOW!!> ")
        ae.write("\n")
        ae.write(input("OT&/" + username + " > "))
        ae.write("\n")
        ae.write("-----------------------")
        ae.write("\n")
        ae.close()
        print("OT&/" + username + " !!SENT!!> ")
        g.write("\n")
        g.write(username + " sent a message to admin.")
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
    with open("level2.txt", "r") as w:
        second = w.read().splitlines()
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

    elif username in second:
        print("Hello, " + username)
        g = open("records.txt", "a")
        g.write("\n")
        g.write(username + " logged in")
        g.close()
        print("You currently have level 2 access")
        print("Limit on command excecution extended to 20")
        f = open("commands.txt", "r")
        print(f.read())
        f.close()
        s = open("level2_co.txt", "r")
        print(s.read())
        s.close()

        for i in range(0,20):
            todo(input("OT&/" + username + "> ")) 


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
    

    


