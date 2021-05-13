# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#import os
from random import randint

def tictactoe(fieldsize=3):

    #cls для Windows, clear для *nix
    #убрал, почему-то не работает при запуске в PyCharm в Windows
    clear_screen = lambda: os.system('cls')

    #инициализируем поле
    field = [["-" for i in range(fieldsize)] for j in range(fieldsize)]

    #показываем поле
    def show_field(field_):
        print(2 * " ", end="")
        for i in range(fieldsize):
            print(f"{i}", end=2 * " ")
        print()
        for i in range(fieldsize):
            print(f"{i} ", end="")
            for j in range(fieldsize):
                print(*field_[i][j], end=2 * " ")
            print()
        print()

    def ask_player(field_):
        while True:
            print("Ваш ход (очерёдность: строка, столбец через Enter):\n")
            turn = [int(input()) for i in range(2)]
            print(f"fieldsize: {fieldsize}")
            print(f"turn: {turn}")

            if (int(turn[0]) or int(turn[1])) > fieldsize:
                print("Координаты должны быть меньше размерности поля!")
                continue
            else:
                #clear_screen()
                field_[turn[0]][turn[1]] = "x"
                return field_, [turn[0], turn[1]]
                break

    def computer_turn(field_):
        nonlocal fieldsize
        #turn_row, turn_col = None, None
        while True:
            turn_row = randint(0, fieldsize-1)
            turn_col = randint(0, fieldsize-1)
            if field_[turn_row][turn_col] != "-":
                continue
            else:
                field_[turn_row][turn_col] = "o"
                return field_, [turn_row, turn_col]
                break

    def uniq(lst):
        last_item = object()
        for item in lst:
            if item == last_item:
                continue
            yield item
            last_item = item

    def check_win(field_, player_, last_turn):
        nonlocal fieldsize

        rows = [[j, last_turn[1]] for j in range(fieldsize)]
        cols = [[last_turn[0], j] for j in range(fieldsize)]

        diags_i, diags_ii, diags_iii, diags_iv = [], [], [], []

        for i in range(fieldsize - last_turn[0]):
            for j in range(fieldsize - last_turn[1]):
                if i == j and (last_turn[0] - i >= 0) and (last_turn[1] - j >= 0):
                    diags_iv.append([last_turn[0] + i, last_turn[1] + j])

        for i in range(fieldsize - last_turn[0]):
            for j in range(fieldsize - last_turn[1]):
                if i == j and (last_turn[0] - i >= 0) and (last_turn[1] - j >= 0):
                    diags_ii.append([last_turn[0] - i, last_turn[1] - j])

        for i in range(fieldsize - last_turn[0]):
            for j in range(fieldsize - last_turn[1]):
                if i == j and (last_turn[0] - i >= 0) and (last_turn[1] - j >= 0):
                    diags_i.append([last_turn[0] + i, last_turn[1] - j])

        for i in range(fieldsize - last_turn[0]):
            for j in range(fieldsize - last_turn[1]):
                if i == j and (last_turn[0] - i >= 0) and (last_turn[1] - j >= 0):
                    diags_iii.append([last_turn[0] - i, last_turn[1] + j])

        print(f"diags_i: {diags_i}")
        print(f"diags_ii: {diags_ii}")
        print(f"diags_iii: {diags_iii}")
        print(f"diags_iv: {diags_iv}")

        diags_i_iii = list(uniq(diags_i+diags_iii))
        diags_ii_iv = list(uniq(diags_ii+diags_iv))

        print(f"diags_i_iii: {diags_i_iii}")
        print(f"diags_ii_iv: {diags_ii_iv}")

        cols_test, rows_test, diags_i_iii_test, diags_ii_iv_test = [], [], [], []

        if player_ == "player":
            mark = "x"
        else:
            mark = "o"
        for lst in rows:
            if field_[lst[0]][lst[1]] != mark:
                rows_test.append(False)
            else:
                rows_test.append(True)
        for lst in cols:
            if field_[lst[0]][lst[1]] != mark:
                cols_test.append(False)
            else:
                cols_test.append(True)
        for lst in diags_i_iii:
            if (field_[lst[0]][lst[1]] != mark) or (len(diags_i_iii) != fieldsize):
                diags_i_iii_test.append(False)
            else:
                diags_i_iii_test.append(True)
        for lst in diags_ii_iv:
            if (field_[lst[0]][lst[1]] != mark) or (len(diags_ii_iv) != fieldsize):
                diags_ii_iv_test.append(False)
            else:
                diags_ii_iv_test.append(True)

        print("test results:", rows_test, cols_test, diags_i_iii_test, diags_ii_iv_test)
        print("test results_:", [all([*rows_test]), all([*cols_test]), all([*diags_i_iii_test]), all([*diags_ii_iv_test])])
        somebody_won =  any([all([*rows_test]), all([*cols_test]), all([*diags_i_iii_test]), all([*diags_ii_iv_test])])
        if somebody_won:
            return player_
        else:
            return None


    player_has_1st_turn = randint(0,1)
    print(f"Крестики-нолики\nРазмер поля: {fieldsize} x {fieldsize}\nВнимание! Компьютер не обучен правилам и ставит нолики случайным образом;)\n")
    show_field(field)
    if player_has_1st_turn:
        print("Первым ходите вы...")
    else:
        print("Первым ходит компьютер...")

    num_turns = 1

    #Главный цикл
    while True:



        print(f"Шаг номер {num_turns}")
        #Если первым ходит игрок
        if player_has_1st_turn:
            #Запрашиваем ход у игрока
            field, last_turn = ask_player(field)
            #clear_screen()
            show_field(field)
            # Проверка на победу после шага игрока
            if check_win(field, "player", last_turn) == "player":
                print("Вы победили!")
                break
            # Ходит компьютер
            field, last_turn = computer_turn(field)
            show_field(field)
            num_turns += 1

            # Проверка на ничью
            if num_turns > fieldsize ** 2:
                print("Ничья!")
                break
            # Проверка на победу после шага компьютера
            if check_win(field, "computer", last_turn) == "computer":
                print("Вы проиграли!")
                break
        #Если первым ходит компьютер
        else:
            #Ходит компьютер
            field, last_turn = computer_turn(field)
            show_field(field)
            # Проверка на победу после шага компьютера
            if check_win(field, "computer", last_turn) == "computer":
                print("Вы проиграли!")
                break
            # Запрашиваем ход у игрока
            field, last_turn = ask_player(field)
            #clear_screen()
            show_field(field)
            num_turns += 1

            # Проверка на ничью
            if num_turns > fieldsize ** 2:
                print("Ничья!")
                break
            # Проверка на победу после шага игрока
            if check_win(field, "player", last_turn) == "player":
                print("Вы победили!")
                break




    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tictactoe(3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
