# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

def tictactoe():

    clear_screen = lambda: os.system('cls')

    field = [["-" for i in range(3)] for j in range(3)]

    def show_field(field):
        print(2 * " ", end = "")
        for i in range(3):
            print(f"{i}", end = 2 * " ")
        print()
        for i in range(3):
            print(f"{i} ", end = "")
            for j in range(3):
                print(*field[i][j],end = 2 * " ")
            print()

    show_field(field)

    def ask_player(field):
        pass

    def computer_step(field):
        pass

    def check_win(field, player):
        pass

    num_steps = 1
    while True:
        #Проверка на ничью
        if num_steps > 9:
            print("Ничья!")
            break

        #Запрашиваем ход у игрока
        field = ask_player(field)
        clear_screen()
        show_field(field)

        # Проверка на победу после шага игрока
        if check_win(field, "player"):
            print("Вы победили!")
            break
        field = computer_step(field)
        show_field(field)

        # Проверка на победу после шага компьютера
        if check_win(field, "computer"):
            print("Вы проиграли!")
            break
        num_steps+=1


    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tictactoe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
