
import json
d = {}
while True:
    try:
        print()
        print("press 1 for register\npress 2 for login\npress 3 for update\npress 4 for delete\npress 5 for exit")
        print()
        def register():
            email = input("enter your email: ")
            if "@gmail.com" in email:
                mo = input("enter your mo.number: ")
                if len(mo) == 10:
                    with open("data.json","w") as data:
                        d[email] = {"mobaile":mo,
                                    "username":input("enter your username: "),
                                    "passwd":input("create your passwd: ")}
                        json.dump(d,data,indent=6)
                        print()
                        print("your registration successful......")
                else:
                    print()
                    print("invalid mo. number")
            else:
                print()
                print("please enter valid email id")
        def login():
            email1 = input("enter your email id: ")
            if "@gmail.com" in email1:
                if email1 in d:
                    with open("data.json","r") as op:
                        data1 = (json.load(op))
                        u = data1[email1]["username"]
                        p = data1[email1]["passwd"]
                        print()
                        print("login to your account")
                        print()
                        loop = "true"
                        while loop == "true":
                            username = input("enter your username: ")
                            if username == u:
                                passwd = input("enter your passwd: ")
                                if passwd == p:
                                    loop = "false"
                                    print()
                                    print("login successfully.......")
                                else:
                                    print()
                                    print("password incorrect!")
                            else:
                                print("username incorrect!")
                                print()
                else:
                    print("your entered email id does not exist")
            else:
                print()
                print("please enter valid email id")
        def update():
            email3 = input("which email id do you want to update: ")
            if "@gmail.com" in email3:
                if email3 in d:
                    with open("data.json","r") as up:
                       data2 = json.load(up)
                       username1 = input("enter your new username: ")
                       passwd1 = input("enter your new passwd: ")
                       data2[email3]["username"] = username1
                       data2[email3]["passwd"] = passwd1
                       with open("data.json","w") as obj:
                           json.dump(data2,obj,indent=6)
                           print()
                           print("updated successfully.......")
                else:
                    print("your entered email id does not exist")
            else:
                print("please enter valid email id: ")
        def delete():
            email4 = input("which email id do you want to delete: ")
            if "@gmail.com" in email4:
                if email4 in d:
                    d.pop(email4)
                    with open("data.json","w") as obj4:
                        json.dump(d,obj4,indent=6)
                        print()
                        print("deleted successfully......")
                else:
                    print("your entered email id does not exist ")
            else:
                print("please enter valid email id: ")
        choice = int(input("enter your choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            login()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
        else:
            break
    except:
        print("please first enter your choice")             