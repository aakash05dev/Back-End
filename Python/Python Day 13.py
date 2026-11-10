
#armstrong numbers(1, 1000)

for i in range(1, 1000):
    num=i
    temp=num
    s=0

    while num > 0:
        r=num%10
        s=s+(r**3)
        num=num//10

    if s == temp:
        print( temp)



#palindrome numbers(1, 1000)

for i in range(1, 1000):
    num=i
    temp=num
    s=0

    while num > 0:
        r=num%10
        s=s*10+r
        num=num//10


        if s == temp:
            print(temp, end=" ")









        
        
