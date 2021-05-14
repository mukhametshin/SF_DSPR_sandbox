import numpy as np


def module_0(num_of_meas=100):  # По умолчанию число попыток измерений равно 100

    """Переработанная функция для угадывания загаданного числа number.
    Делим отрезок (max - min) пополам и сравниваем значение посередине с number.
    Далее продолжаем деление и сравнение в рекурсии"""
    def game_core_v3(number, count_=0, min_=1, max_=101):
        count_ += 1  # Число попыток
        while True:
            predict = min_ + (max_ - min_) // 2
            #  для отладки
            #  print(f"number, count, guess = {number}, {count_}, {predict}")
            if predict == number:  # Когда число отгадано, возвращаем число попыток
                return count_
            return game_core_v3(number, count_, min_, predict) if predict > number \
                else game_core_v3(number, count_, predict, max_)  # Вызов функции в рекурсии
            # либо от левой части отрезка, либо от правой, в зависимости от результата сравнения

    def random_gen():
        """Генерируем случайное число и возвращаем его генератором.
        RANDOM SEED не фиксируем (как в примере), т.к. иначе генерируется одно и то же число"""
        while True:
            yield np.random.randint(1, 101)

    def score_game(game_core, num_of_meas_):
        """Слегка доработанная функция для вызова функции game_core() игры
        и подсчёта среднего количества попыток. Число измерений передаётся через аргумент num_of_meas_"""
        count_ls = []  # Инициализируем счётчик для числа попыток угадывания
        for counter in range(num_of_meas_):  # Счётчик измерений
            number = random_gen()  # Забираем случайное число из генератора
            count_ls.append(game_core(number.__next__()))  # Добавляем в список число попыток угадывания
        score = (np.mean(count_ls))  # Считаем среднее число попыток за num_of_meas_ измерений
        print(f"Ваш алгоритм угадывает число в среднем за {score} ~ {np.ceil(score):.0f} попыток. "
              f"Усреднение по {num_of_meas_} измерений.")

    score_game(game_core_v3, num_of_meas)  # Проводим, собственно, тест


if __name__ == '__main__':
    module_0(10000)  # Аргумент функции - число измерений (по умолчанию 100)
