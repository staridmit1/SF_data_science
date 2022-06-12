"""Игра угадай число
Компьютер сам загадывает число и сам угадывает
"""

import numpy as np

def random_predict(number: int=1) -> int:
    """Random guessing a number

    Args:
        number (int, optional): Chosen number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0
    
    while True:
        count+=1
        predict_number = np.random.randint(1, 101) # computer predicted number
        if number == predict_number:
            break #exit cycle
    return(count)

# print(f'Number of tries: {random_predict(10)}')

def score_game(random_predict) -> int:
    """What is the average speed of guessing for 1000 cycles

    Args:
        random_predict (_type_): Guessing function

    Returns:
        int: Avg number of tries
    """
    count_ls = []
    np.random.seed(1) # Fixing random seed for repeatition
    random_array = np.random.randint(1, 101, size=(1000)) # Giving a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Your algorithm is guessing the number on average in: {score} tries')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)