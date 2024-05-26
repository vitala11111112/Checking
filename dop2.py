def CheckThePassword(password):  
    isValid = 0
    if len(password) >= 8:
        isValid = 1
    return isValid
def CheckThePassword1(password):
    b = "qwertyuiopasdfghjklzxcvbnm"
    isValid = 0
    for i in range(len(password)):
        if isinstance(password[i],str) and password[i] in b:
            isValid = 1
    return isValid
def CheckThePassword2(password):
    isValid = 0
    b = ["!","#","№",";","@","%"]
    for i in range(len(password)):
        if password[i] in b:
            isValid = 1
    return isValid

if __name__ == '__main__':
    password = input("Please enter your passsword")
    isValid = CheckThePassword(password)
    isValid1 = CheckThePassword1(password)
    isValid2 = CheckThePassword2(password)
    if  isValid==1 and isValid1== 1 and isValid2 == 1:
        print("Password is valid")
    else:
        print("Password is not valid")