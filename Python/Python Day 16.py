#generate even numbers:

def even_generator(numbers):
    for number in numbers:
        if number%2 ==0:
            yield number


my_numbers=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
result=even_generator(my_numbers)

print(next(result))

print(next(result))

print(next(result))

print(next(result))

print(next(result))

