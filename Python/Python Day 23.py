import time
import threading

def customer1():
    i=1
    while i <=3:
        print("customer1: checking balance", i)
        time.sleep(3)
        i+=1

def customer2():
    i=1
    while i <=3:
        print("customer2: withdrawing amount", i)
        time.sleep(2)
        i+=1


def customer3():
    i=1
    while i <=3:
        print("customer3: checking transaction", i)
        time.sleep(1)
        i+=1

t1=threading.Thread(target=customer1)
t2=threading.Thread(target=customer2)
t3=threading.Thread(target=customer3)

t1.start()
t2.start()
t3.start()
