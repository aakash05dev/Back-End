#virtual function:

class mobile1:

    def mobile_details(self):
        print("Mobile Brand : Vivo")

    def model(self):
        print("mobile model : normal model")


class mobile2(mobile1):
    def model(self):
        print("Mobile Model : Vivo T4 5G")


m2=mobile2()

m2.mobile_details()
m2.model()
print("\n------------------------------")



#abstract function:

from abc import ABC, abstractmethod

class Insta(ABC):

    @abstractmethod
    def uploadphoto(self):
        pass
    
    @abstractmethod
    def reelsupload(self):
        pass

    @abstractmethod
    def likepost(self):
        pass

class user(Insta):

    def uploadphoto(self):
        print("photo uploaded successfully")

    def reelsupload(self):
        print("reels uploaded successfully")

    def likepost(self):
        print("liked post ")

u=user()

u.uploadphoto()
u.reelsupload()
u.likepost()




    

    
































