from random import randrange
from termcolor import colored


def init_game():

    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    combinations = [
        [1, 2, 3],
        [1, 4, 7],
        [1, 5, 9],
        [2, 5, 8],
        [3, 6, 9],
        [3, 5, 7],
        [4, 5, 6],
        [7, 8, 9],
    ]

    cpu_moves = []
    user_moves = []

    game_over_message = colored(f"¡Has perdido!", "red")
    win_message = colored(f"¡Has ganado!", "green")

    turn_number = 0

    def print_board():
        for row in board:
            print(f"| {row[0]} - {row[1]} - {row[2]} |")

    def check_number_in_range(n):
        if n > 9 or n < 1:
            return False

        return True

    def select_option_on_board(option, user):
        board[option[0]][option[1]] = (
            colored("0", "green") if user else colored("X", "red")
        )
        return

    def random_move():
        return randrange(1, 9)

    def check_availability(option):
        for row in board:
            if option in row:
                return [board.index(row), row.index(option)]

        return False

    def check_win(moves):
        for combination in combinations:
            counter = 0
            for user_option in moves:
                if user_option in combination:
                    counter += 1

            if counter == 3:
                return True
            else:
                counter = 0

        return False

    def check_if_game_ended(moves=[], user=False):
        if turn_number >= 3 and check_win(moves):
            print(win_message if user else game_over_message)
            print_board()
            return quit()
        if turn_number == 5:
            print(colored("¡Empate!", "blue"))
            print_board()
            return quit()

        return

    def user_move():

        option = False
        attempts = 0
        while (
            check_number_in_range(option) == False
            or (option in user_moves)
            or (option in cpu_moves)
        ):
            attempts += 1

            if attempts > 1:
                print(colored("¡Aségurate de escoger un número libre!", "yellow"))
            try:
                option = int(input("Escoge casilla(por número): "))
            except:
                print(
                    colored(
                        "Has de ingresar un número del 1 al 9 (ambos incluidos)",
                        "yellow",
                    )
                )

        availability = check_availability(option)

        select_option_on_board(availability, True)

        user_moves.append(option)

        check_if_game_ended(user_moves, True)
        return init_turn()

    # 2 movimiento de la CPU
    def cpu_move():
        if turn_number == 1:
            select_option_on_board([1, 1], False)
            cpu_moves.append(5)
            print("===========")
            print_board()
            return user_move()

        availability = False

        while availability == False:
            availability = check_availability(random_move())

        cpu_moves.append(board[availability[0]][availability[1]])

        select_option_on_board(availability, False)

        check_if_game_ended(cpu_moves, False)

        print("============")
        print_board()
        return user_move()

    def init_turn():
        nonlocal turn_number #declaramos que el ámbito de la variable es global
        turn_number += 1 #sumamos turno
        print("============")
        print_board() #pintamos el tablero
        return cpu_move() #inicia siempre CPU

    init_turn()

init_game()
