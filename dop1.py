def CheckThePassword(password):
    b = "qwertyuiopasdfghjklzxcvbnm"
    isValid = False
    if len(password) >= 8:
        for i in range(len(password)):
            if isinstance(password[i],str) and password[i] in b:
                isValid = True
    return isValid

if __name__ == '__main__':
    password = input("Please enter your passsword")
    isValid = CheckThePassword(password)
    if isValid:
        print("Password is valid")
    else:
        print("Password is not valid")