#armstrong numbers: 153

#no parameter, no return type

def armstrong():
    num=int(input("enter a number:"))
    temp=num
    sum=0

    while num>0:
        r=num%10
        sum=sum+r**3
        num=num//10


    if temp == sum:
        print("armstrong number")
    else:
        print("not armstrong number")


armstrong()




#with parameter, no return type


def armstrong(num):
    temp=num
    sum=0

    while num>0:
        r=num%10
        sum=sum+r**3
        num=num//10



    if temp==sum:
        print("armstrong number")
    else:
        print("not armstrong number")


a=int(input("enter a number:"))
armstrong(a)
        



#with parameter, with return type

def armstrong(num):
    temp=num
    sum=0

    while num>0:
        r=num%10
        sum=sum+r**3
        num=num//10


    if temp==sum:
         return "armstrong number"

    else:
        return "not amstrong number"


a=int(input("enter a number:"))
result=armstrong(a)
print(result)



#no parameter, with type

def armstrong():
    num=int(input("enter a number:"))
    temp=num
    sum=0

    while num>0:
        r=num%10
        sum=sum+r**3
        num=num//10


    if temp==sum:
         return "amstrong number"
    else:
         return "not amstrong number"
        
result=armstrong()
print(result)
















































