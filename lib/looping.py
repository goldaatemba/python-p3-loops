#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!") # happy_new_year()



def square_integers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared
# print(square_integers([1, 2, 3, 4, 5]))  # Should output [1, 4, 9, 16, 25]


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i) # fizzbuzz()

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


def square_integers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Uncomment the lines below to test
# happy_new_year()
# print(square_integers([1, 2, 3, 4, 5]))
# fizzbuzz()

