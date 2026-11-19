#1.multi level inheritance

class college:
    def college_name(self):
        print(" college name: TCAS arts & science college ")

    def college_location(self):
        print(" college location: Tirukkoilur ")


class department(college):
    def department_name(self):
        print(" department name: computer science ")

    def degree(self):
        print(" degree: B.Sc" )


class student(department):
    def student_name(self):
        print(" student name: Akash ")

    def student_id(self):
        print(" student Id: 105")

obj=student()

obj.college_name()
obj.college_location()
obj.department_name()
obj.degree()
obj.student_name()
obj.student_id()

print("\n --------------------------------------")



#multiple inheritance:

class laptop:
    def laptop_on(self):
        print(" laptop power on ")

    def open_browser(self):
        print(" browser open ")

class internet:
    def connect_wifi(self):
        print(" wifi connected ")

    def internet_speed(self):
        print(" internet connection is available ")

class onlineclass(laptop, internet):
    def attend_class(self):
        print(" online class started ")

    def submit_assingment(self):
        print(" Assignment sumbited successfully ! ")


obj=onlineclass()


obj.laptop_on()
obj.open_browser()
obj.connect_wifi()
obj.internet_speed()
obj.attend_class()
obj.submit_assingment()

