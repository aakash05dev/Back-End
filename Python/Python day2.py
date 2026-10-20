# Program 1: Student Grade

mark = int(input("Enter your mark: "))

match mark:
    case m if m >= 35:
        print("Pass")
    case _:
        print("Fail")


# Program 2: Favourite Sport

name = input("Enter your name: ")

match name:
    case "Akash":
        print("Cricket")
    case "Kumar":
        print("Football")
    case "Raja":
        print("Kabaddi")
    case _:
        print("Invalid name")
