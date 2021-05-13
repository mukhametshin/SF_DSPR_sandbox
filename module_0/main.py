import numpy as np


def module_0():

    def game_core_v3(number, count_=0, min_=0, max_=101):
        count_ += 1
        while True:
            predict = min_ + (max_ - min_) // 2
            #print(f"count, guess = {count_}, {predict}")
            if predict == number:
                return count_
            return game_core_v3(number, count_, min_, predict) if predict > number \
                else game_core_v3(number, count_, predict, max_)

    def random_gen():
        np.random.seed(1)  # Фиксируем RANDOM SEED как в примере
        while True:
            yield int(np.random.randint(1, 101))

    def score_game(game_core, count_):
        count_ls = []
        for counter in range(count_):
            number = random_gen()
            count_ls.append(game_core(number.__next__()))
        score = int(np.mean(count_ls))
        print(f"Ваш алгоритм угадывает число в среднем за {score} попыток. "
              f"Усреднение по {count_} измерений.")
        return score

    score_game(game_core_v3, 100000)
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    module_0()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
