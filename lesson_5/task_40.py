#!/usr/bin/python
#
# 40. Создайте программу для игры в ""Крестики-нолики"".
#

import sys

BOARD_ROWS = 3
BOARD_COLS = 3


def banner():
    print(' Крестики-Нолики')
    print('-----------------')


def draw_board(board):
    banner()

    for row in range(BOARD_ROWS):
        print('|', end='')

        for col in range(BOARD_COLS):
            print(f'{board[row][col]}|', end='')
        print()


def is_won(board, player):
    for row in range(BOARD_ROWS):
        count = 0
        for col in range(BOARD_COLS):
            if board[row][col] == player:
                count += 1
        if count == BOARD_COLS:
            return True

    for col in range(BOARD_COLS):
        count = 0
        for row in range(BOARD_ROWS):
            if board[row][col] == player:
                count += 1
        if count == BOARD_ROWS:
            return True

    count = 0
    for i in range(BOARD_ROWS):
        if board[i][i] == player:
            count += 1
    if count == BOARD_ROWS:
        return True

    count = 0
    for i in range(BOARD_ROWS):
        if board[i][BOARD_ROWS - i - 1] == player:
            count += 1
    if count == BOARD_ROWS:
        return True

    return False


def cells_available(board):
    availables = []
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] != 'X' and board[row][col] != 'O':
                availables.append(int(board[row][col]))
    return availables


def is_empty_cell(board, move):
    row = (move - 1) // BOARD_ROWS
    col = (move - 1) % BOARD_COLS
    return board[row][col].isdigit()


def is_over(board):
    return is_won(board, 'X') or is_won(board, 'O') or not cells_available(board)


def do_move(board, move, player):
    row = (move - 1) // BOARD_ROWS
    col = (move - 1) % BOARD_COLS
    board[row][col] = player


def enter_move(board, player_name):
    availables = cells_available(board)

    while True:
        move = int(
            input(f'{player_name}, сделайте свой ход, выбрав число из {availables}: '))
        if move in availables:
            break
        else:
            print('Нет такого хода!')

    return move


def main():
    banner()
    print()

    main_player_name = input('Введите ваше имя: ')
    opponent_player_name = input('Введите имя противника: ')

    while True:
        main_player = input(
            f'{main_player_name}, вы предпочитаете играть крестиками (X) или ноликами (O)? ').upper()
        if main_player == 'X' or main_player == 'O':
            break

    if main_player == 'O':
        main_player_name, opponent_player_name = opponent_player_name, main_player_name

    board = [[str(row * BOARD_ROWS + 1 + col)
              for col in range(BOARD_COLS)] for row in range(BOARD_ROWS)]

    draw_board(board)

    while not is_over(board):
        move = enter_move(board, main_player_name)
        do_move(board, move, 'X')
        draw_board(board)

        if is_over(board):
            if is_won(board, 'X'):
                print(f'{main_player_name} победил!')
                break
            if not cells_available(board):
                print('Ничья!')
                break

        move = enter_move(board, opponent_player_name)
        do_move(board, move, 'O')
        draw_board(board)

        if is_over(board):
            if is_won(board, 'O'):
                print(f'{opponent_player_name} победил!')
                break
            if not cells_available(board):
                print('Ничья!')
                break


if __name__ == '__main__':
    main()
