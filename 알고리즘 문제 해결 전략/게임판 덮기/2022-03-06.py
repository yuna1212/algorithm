"""
시작 시간: 2022년 3월 8일 오후 10시
소요 시간: 2시간
풀이 방법: 
    알고리즘은 맞는데, 구현을 못함
    좀 더 단순하게 구현할 수 있는 방법 찾기
"""
import copy
def input_data():
    h, _ = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(list(input()))
    return board

def find_possible_way1(board, row_idx, column_idx):
    board_width = len(board)
    board_height = len(board[0])
    if row_idx + 1 > board_height:
        return None
    if column_idx + 1 > board_width:
        return None
    if board[row_idx][column_idx+1] == "." and board[row_idx+1][column_idx+1] == ".":
        new_board = copy.deepcopy(board)
        new_board[row_idx][column_idx] = "#"
        new_board[row_idx][column_idx+1] = "#"
        new_board[row_idx+1][column_idx+1] = "#"
        return new_board
    return None
def find_possible_way2(board, row_idx, column_idx):
    board_height = len(board[0])
    if row_idx + 1 > board_height:
        return None
    if column_idx - 1 < 0:
        return None
    if board[row_idx+1][column_idx-1] == "." and board[row_idx+1][column_idx] == ".":
        new_board = copy.deepcopy(board)
        new_board[row_idx][column_idx] = "#"
        new_board[row_idx+1][column_idx-1] = "#"
        new_board[row_idx+1][column_idx] = "#"
        return new_board
    return None
def find_possible_way3(board, row_idx, column_idx):
    board_width = len(board)
    board_height = len(board[0])
    if row_idx + 1 > board_height:
        return None
    if column_idx + 1 > board_width:
        return None
    if board[row_idx+1][column_idx] == "." and board[row_idx+1][column_idx+1]==".":
        new_board = copy.deepcopy(board)
        new_board[row_idx][column_idx] = "#"
        new_board[row_idx+1][column_idx] = "#"
        new_board[row_idx+1][column_idx+1] = "#"
        return new_board
    return None
def find_possible_way4(board, row_idx, column_idx):
    board_width = len(board)
    board_height = len(board[0])
    if row_idx + 1 > board_height:
        return None
    if column_idx + 1 > board_width:
        return None
    if board[row_idx][column_idx+1] == "." and board[row_idx+1][column_idx] == ".":
        new_board = copy.deepcopy(board)
        new_board[row_idx][column_idx] = "#"
        new_board[row_idx+1][column_idx] = "#"
        new_board[row_idx][column_idx+1] = "#"
        return new_board
    return None

def find_first_white(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                return i, j
    return -1, -1
def find_number_solutions(board):
    row_idx, column_idx = find_first_white(board)
    if row_idx < 0: # 모두 덮인 경우
        return 1
    
    number_of_solutions = 0
    board_sets = [find_possible_way1(board, row_idx, column_idx),
                  find_possible_way2(board, row_idx, column_idx),
                  find_possible_way3(board, row_idx, column_idx),
                  find_possible_way4(board, row_idx, column_idx)]

    for board_set in board_sets:
        if board_set: # 덮을 수 있는 경우
            number_of_solutions += find_number_solutions(board_set)
        
    return number_of_solutions

def solution():
    board = input_data()
    return find_number_solutions(board)

print(solution())