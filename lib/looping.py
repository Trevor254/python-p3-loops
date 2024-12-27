#!/usr/bin/env python3

def happy_new_year():
   num = 10
   while num > 0:
        print(num)
        num -= 1  # Decrease the number by 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [x**2 for x in int_list]
    

def fizzbuzz():
    # code goes here!
        for num in range(1, 101):  # Loop through numbers 1 to 100
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
    
