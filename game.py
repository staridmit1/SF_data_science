"""Игра угадай число"""

import numpy as np

number = np.random.randint(1, 101) # take a number for guessing game

# Number of tries
count = 0

while True:
    count += 1
    predict_number = int(input("Enter a number from 1 to 100: "))
    
    if predict_number > number:
        print("Number should be smaller")
    elif predict_number < number:
        print("Number should be bigger")
    else:
        print(f"You've picked a right number! It is {number}, in {count} tries")
        break # end of function
