def chooseOption():
    option=input("New User: (a), Update User: (b), Delete User: (c)")
    if option == "a":
        createNewUser()
    elif option == "b":
        login()
    elif option == "c":
        deleteUser()
    else:
        quit()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
d={}
list=[]
for id in range(1,11):
    list.append(id)
print(list)
i=0
def createNewUser():
    username=input("Enter Name: ")
    userphone=int(input("Enter Phone: "))
    global i
    while i < len(list):
        d[list[i]]=[username,userphone]
        
        print(f"Successfully created the user with user name and phone number as {d[list[i]]}")
        print(f"Your login key is {list[i]}")
        print(d)
        i=i+1
        chooseOption()
    else:
        print("IDs Over")
        quit()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def login():
    a = int(input("Enter ID to view details: "))
    print(d[a])
    print("update name | update phone number?")
    u = input("y for name/n for number: ")
    if u == "y":
        d[a][0] = input("Enter new username: ")
        print(d[a])
        print(d)
        chooseOption()
    elif u == "n":
        d[a][1]= int(input("Enter new number: "))
        print(d[a])
        print(d)
        chooseOption()
    else:
        chooseOption()
def deleteUser():
    led = int(input("Enter ID to delete the user: "))
    if led in d:
        print(f"We are going to delete {d[led]}")
        del d[led]
        print(f"Updated details are {d}")
        chooseOption()
    else:
        print("Given ID not created")
        chooseOption()
chooseOption()
        
