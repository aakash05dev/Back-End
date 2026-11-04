#odd or even using lamda

result = lambda a: 'even' if a % 2 == 0 else 'odd'
print(result(7))




#recursive function

def factorial(number):
    if number == 1:
        return 1

    else:
        result = number * factorial(number - 1)
        return result

print('factorial', factorial(5))

