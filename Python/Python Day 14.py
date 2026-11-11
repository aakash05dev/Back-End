#mplement decorator for your own requirement:

def internet(func):
    def innerfunction():
        print('Internet Connected')
        func()
        print('Data Usage Completed')

    return innerfunction

@internet
def browsing():
    print('Browsing Started')
    print('Opening Website')

browsing()


#realtime example for decorator:

def service_charge(func):
    def innerfunction():
        print('Welcome to Restaurant')
        func()
        print('Service Charge: Rs.100')
        print('Thank You !')

    return innerfunction

@service_charge
def bill():
    print('Food Bill: Rs:530')
bill()


        
