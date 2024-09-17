username = ["haha", "halo"]
password = ["haha", "far"]
balance = 0
loginusr = None

def menu():
    while True:
        print("===============Steam CLI===============")
        print("1. Login")
        print("2. Register")
        print("3. Buy Game")
        print("4. Redeem Code")
        print("5. Exit")
        userSelect = input("\nSelect menu(1,2,3,4,5): ")
        print("=======================================")

        if userSelect == "1":
            login()
        elif userSelect == "2":
            register()
        elif userSelect == "3":
            buyGame()
        elif userSelect == "4":
            redeem()
        elif userSelect == "5":
            print("Exit the program")
            exit()
        else: 
            print("Error")

def login():
    usernameInput = input("Username: ")
    passInput = input("Password: ")
    for i in range(len(username)):
        if username[i] == usernameInput and password[i] == passInput:
            global loginusr 
            loginusr = username[i]
            print(f"Login as {username[i]} Success")
            return 
    print("Login failed")

def register():
    global username
    global password
    InputUsr = input("Username: ")
    InputPass = input("Password: ")

    for i in username:
        if InputUsr == i:
            print("User already registered")
            return
    username.append(InputUsr)
    password.append(InputPass)

    print("Registration successful!")

def buyGame():
    global balance
    if loginusr == None:
        print("Not loged in")
        return
    print("\t\tBuy game")
    print(f"Balance: {balance}")
    print("1.Calculator Game")
    print("2.Flag")
    usrInput = input("Select Game(1,2): ")
    if usrInput == "1" and balance > 1000:
        balance = balance - 1000
        print("Buy Game successful!")
    elif usrInput == "1" and balance < 1000:
        print("not enough balance")
    elif usrInput == "2" and balance > 100000:
        balance = balance - 100000
        print("Buy Game successful! \nFlag is the redeem code")
    elif usrInput == "2" and balance < 100000:
        print("not enough balance")
    else:
        print("Error")

def redeem():
    global balance
    if loginusr == None:
        print("Not loged in")
        return
    inpCode = input("Code: ")
    inpList = list(inpCode)

    if len(inpCode) != 21:
        print("Invalid code")
        return

    code = ['K', '3', 'M', 'O', 'E', '3', '3', 'c', 'T', '{', '4', 'T', 'd', 'h', '_', 'D', 'R', '0', 'L', '_', '}']
    swaps = [
    (0,2), (3,1), (18,12), (20,1), (11,5), (6,9), (10,15),
    (16,7), (18,8), (6,10), (14, 5), (6, 19), (18,1), (20,18)
    ]

    for swap in swaps:
        inpList[swap[0]], inpList[swap[1]] = inpList[swap[1]], inpList[swap[0]]

    if ''.join(inpList) == ''.join(code):
        balance += 100000000000
        print("Redeem Code Successfull!")
        print(f"Current Balance: {balance}")
    else: 
        print("Invalid Code")
        return
    
    


if __name__ == "__main__":
    menu()