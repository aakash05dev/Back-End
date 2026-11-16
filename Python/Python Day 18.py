class student:

    def setdetails(self):
        self.name=input("enter a student name:")
        self.age=int(input("enter student age:"))
        self.course=input("enter course name:")
        self.mark=int(input("enter student mark:"))


    def getdetails(self):
        print("\n---STUDENT DETAILS----")
        print("student name:", self.name)
        print("student age:", self.age)
        print("course name:", self.course)
        print("student mark:", self.mark)

s1=student()

s1.setdetails()
s1.getdetails()
