import random


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

    turn_number = 0

    # 1
    def print_board():
        for row in board:
            print(row)

    def check_number_in_range(n):
        if n > 9 or n < 1:
            return False

        return True

    def select_option_on_board(option, user):
        board[option[0]][option[1]] = "o" if user else "x"
        return

    def random_move():
        return random.randrange(1, 9)

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

    def user_move():

        option = False

        while check_number_in_range(option) == False or (option in user_moves):
            option = int(input("Escoge casilla(por número): "))

        availability = check_availability(option)

        select_option_on_board(availability, True)

        user_moves.append(option)

        if turn_number >= 3 and check_win(user_moves):
            print("Has ganado con " + str(turn_number))
            return print_board()
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

        if turn_number >= 3 and check_win(cpu_moves):
            print("Has perdido con " + str(turn_number))
            return print_board()

        print("============")
        print_board()
        return user_move()

    def init_turn():
        nonlocal turn_number
        turn_number += 1
        print("============")
        print_board()
        return cpu_move()

    init_turn()


init_game()
