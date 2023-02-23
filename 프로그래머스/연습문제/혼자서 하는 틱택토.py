"""
시작 시간: 2023-02-23 09:26 PM
소요 시간: 1시간 10분
풀이 방법: 어떤 예외들이 있을지 꼼꼼하게 살펴보기
"""
BOARD_SIZE=3
FIRST="O"
SECOND="X"
def check_row(player):
    global BOARD
    for line in BOARD:
        if line.count(player) == BOARD_SIZE:
            return True

    return False

def check_column(player):
    global BOARD
    for i in range(BOARD_SIZE):
        number = 0

        for j in range(BOARD_SIZE):
            number += BOARD[j][i] == player

        if number == BOARD_SIZE:
            return True

    return False

def check_cross(player):
    global BOARD
    up_number = 0
    down_number = 0

    for i in range(BOARD_SIZE):
        up_number += BOARD[i][BOARD_SIZE - i - 1] == player
        down_number += BOARD[i][i] == player

    if up_number == BOARD_SIZE or down_number == BOARD_SIZE:
        return True
    return False


def is_winner(player):
    if check_row(player) or check_column(player) or check_cross(player):
        return True
    return False

def count_pieces(player):
    global BOARD
    ret = 0
    for line in BOARD:
        ret += line.count(player)
    return ret


def solution(board):
    global BOARD, FIRST
    BOARD = board

    num_of_first = count_pieces(FIRST)
    num_of_second = count_pieces(SECOND)

    if num_of_second > num_of_first or num_of_first - num_of_second > 1:
        return 0

    first_is_winner = is_winner(FIRST)
    if first_is_winner and num_of_first <= num_of_second:
        return 0

    second_is_winner = is_winner(SECOND)
    if second_is_winner and num_of_first > num_of_second:
        return 0

    if first_is_winner and second_is_winner:
        return 0

    return 1

