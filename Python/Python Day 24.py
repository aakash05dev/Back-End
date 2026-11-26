class PasswordException(Exception):
    pass


password=input("enter your password : ")
try:
    if password == "Akash123":
        raise PasswordException(" login successfully! ")

    else:
        print(" invalid password ")


except PasswordException as ex:
    print(ex)
