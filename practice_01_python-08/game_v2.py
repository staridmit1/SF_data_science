"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # задаем глобальные переменные
    count = 0
    min_range = 1
    max_range = 101
    
    predict_number = np.random.randint(min_range, max_range)  # предполагаемое число
    
    while True:
        count += 1
        if number == predict_number:
            break  # выход из цикла если угадали
        else:
            if number > predict_number:
                min_range = predict_number # сдвигаем левую границу диапазона до выбранного числа
                predict_number = np.random.randint(min_range, max_range)
            elif number < predict_number:
                max_range = predict_number # сдвигаем правую границу диапазона до выбранного числа
                predict_number = np.random.randint(min_range, max_range)
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
