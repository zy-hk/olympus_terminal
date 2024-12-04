import os
import glob
import csv


passcode = "thisisamystery"
password = "lunch:)hour"

def load_users(filename='users.csv'):
    users = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # Ensure it's not an empty row
                users[row[0]] = row[1]  # username: hashed_password
    return users

def account_create(username, password, filename='users.csv'):
    print("Please remember your password.")
    with open(filename, 'a', newline='') as csvfile: 
        writer = csv.writer(csvfile)
        writer.writerow([username, password])
    f = open("users.txt", "a")
    f.write(username + "\n")
    f.close()
    g = open("records.txt", "a")
    g.write("\n")
    g.write("New user registered: " + username + "\n")
    g.close()
    em = open("emails/" + username + "@omail.com.txt", "x")
    em.write("Omail --- " + username + "@omail.com")
    em.close()
    p = open("everybody.txt", "a")
    p.write("\n")
    p.write(username + "@omail.com" + "\n")
    p.close()
    print("You are now registered as a user, " + username)
    print("You currently have access authority: level 1")
    print("Your email account is: " + username + "@omail.com")
    print("admin email is admin@omail.com")


def sign_in(username, password, filename="users.csv"):
    if username == "admin":
        print("hello, admin.")
        return True
    else :
        users = load_users(filename)
        if username in users:
            password_saved = users[username]
            if password_saved == password:
                print("Access granted.")
                return True
            else:
                print("Invalid password.")
                return False
        else:
            print("User not found.")
        return False

def help_menu():
    print("Available commands:")
    print(" - inbox: opens inbox")
    print(" - read: reads email")
    print(" - email: writes email")
    print(" - draw: rename a file")
    print(" - cook: write to a file")
    print(" - boom: create a new file")
    print(" - shoot: delete a file")
    print("- hack: reads a file")
    print("- board: view the public board")
    print("- whoami: view username")
    print("- padlock: view password")
    print("- leave: exit terminal")

    # Add more commands here.


def todo(action):
    g = open("records.txt", "a")
    if action == "help":
        help_menu()
    if action == "leave":
        g.write("\n")
        g.write(username + " left")
        g.write("\n")
        exit()
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
    if action == "everybody":
        lt = open("everybody.txt", "r")
        print(lt.read())
        lt.close()
        g.write("\n")
        g.write(username + " checked everybody.txt")
        return True
    if action == "inbox":
        ib = open("emails/" + username + "@omail.com.txt", "r")
        print(ib.read())
        ib.close()
        g.write("\n")
        g.write(username + " checked their email")
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
        return True
    if action == "email":
        person = input("OT&/" + username + " !!RECIPIENT EMAIL ADRESS!!> ")
        ae = open("emails/" + person + ".txt", "a")
        ae.write("\n")
        ae.write("\n")
        ae.write("-----------------------")
        ae.write("\n")
        ae.write("Message from  " + username + "@omail.com")
        ae.write("\n")
        ae.write("------")
        ae.write("\n")
        ae.write(input("OT&/" + username + " !!EMAIL SUBJECT!!> "))
        ae.write("\n")
        ae.write("------")
        ae.write("\n")
        print("OT&/" + username + " !!WRITE EMAIL CONTENT BELOW!! (press Ctrl+Z to enter)> ")
        content = []
        while True:
            try:
                line = input()
                content.append(line)
            except EOFError:
                break
        
        ae.write("\n".join(content))
        ae.write("-----------------------")
        ae.write("\n")
        ae.close()
        print("OT&/" + username + " !!SENT!!> ")
        g.write("\n")
        g.write(username + "@omail.com sent an email to " + person + " .")
        return True
    g.close()

    

tmpvar = input("Sign in or Create Account? (s/c) ")
print("type (e) to leave")

if tmpvar == "c":
    print("Usernames should be noncapitalised and a length of 4 letters without spaces")
    account_create(username = input("Create username: "), password = input("Create password: "))
    exit()

elif tmpvar == "s":
    correct = sign_in(username = input("Username: "), password = input("Password: "))

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
    

    


