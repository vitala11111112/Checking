import random

def CheckThePassword(password):
    isValid = False
    if len(password) >= 8:
        isValid = True
        
    return isValid

if __name__ == '__main__':
    password = input("Please enter your passsword")
    isValid = CheckThePassword(password)
    if isValid:
        print("Password is valid")
    else:
        print("Password is not valid")