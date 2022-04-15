"""
시작 시간: 2022년 4월 15일 오후 5시 50분
소요 시간: 1시간 50분
풀이 방법:
    격자공간도 20*20이고, 4개 선택지에 대해 최대 5번 움직인다는게 굉장히 공간이 작기 때문에
    brute force로 푸는 것 같다에서 시작함
    
    근데 매번 deepcopy 4번씩 해야한다는게 의심스러웠다,,
    그치만 해봐야 5*4=20이고, 카피하는 대상도 400개밖에 안되기 때문에 해봐야 8K번임
    그렇다고 보드를 움직이는 것에서 엄청 시간 잡아먹는것도 아니다(O(N^2))
    
    주어진 공간이 매우 작기에 가능
    
    알고리즘 떠올리는 것도 시간 오래걸리고, 대부분 비슷한 코드 복붙하는데도 시간이 걸렸다.
"""
import sys
from copy import deepcopy
def input_data(n):
    grid = []
    for _ in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))
    return grid

def to_upper(board):
    n = len(board)
    last = 0
    for i in range(0, n):
        last = board[0][i]
        new_nums = []
        for j in range(1, n):
            now = board[j][i]
            if now == 0:
                continue
            if last == now:
                new_nums.append(last*2)
                last = 0
            else:
                if last != 0:
                    new_nums.append(last)
                last = now
        if last > 0:
            new_nums.append(last)
        j = 0
        for j in range(len(new_nums)):
            board[j][i] = new_nums[j]
        for j in range(len(new_nums), n):
            board[j][i] = 0
    return

def to_down(board):
    n = len(board)
    last = 0
    for i in range(0, n): # 열
        last = board[-1][i]
        new_nums = []
        for j in range(n-2, -1, -1): # 행
            now = board[j][i]
            if now == 0:
                continue
            if last == now:
                new_nums.append(last*2)
                last = 0
            else:
                if last != 0:
                    new_nums.append(last)
                last = now
        if last > 0:
            new_nums.append(last)
        j = 0
        for j in range(len(new_nums)):
            board[n-j-1][i] = new_nums[j]
        for j in range(0, n-len(new_nums)):
            board[j][i] = 0
    return
    
def to_left(board):
    n = len(board)
    last = 0
    for i in range(0, n):
        last = board[i][0]
        new_nums = []
        for j in range(1, n):
            now = board[i][j]
            if now == 0:
                continue
            if last == now:
                new_nums.append(last*2)
                last = 0
            else:
                if last != 0:
                    new_nums.append(last)
                last = now
        if last > 0:
            new_nums.append(last)
        j = 0
        for j in range(len(new_nums)):
            board[i][j] = new_nums[j]
        for j in range(len(new_nums), n):
            board[i][j] = 0
    return

def to_right(board):
    n = len(board)
    last = 0
    for i in range(0, n): # 열
        last = board[i][-1]
        new_nums = []
        for j in range(n-2, -1, -1): # 행
            now = board[i][j]
            if now == 0:
                continue
            if last == now:
                new_nums.append(last*2)
                last = 0
            else:
                if last != 0:
                    new_nums.append(last)
                last = now
        if last > 0:
            new_nums.append(last)
        j = 0
        for j in range(len(new_nums)):
            board[i][n-j-1] = new_nums[j]
        for j in range(0, n-len(new_nums)):
            board[i][j] = 0
    return

def solution(grid, count):
    if count < 5:
        up = deepcopy(grid)
        to_upper(up)
        
        down = deepcopy(grid)
        to_down(down)
        
        left = deepcopy(grid)
        to_left(left)
        
        right = deepcopy(grid)
        to_right(right)
        
        count += 1
        return max(solution(up, count), solution(down, count), solution(left, count), solution(right, count))
    else:
        
        return max(map(max, grid))
grid = input_data(int(input()))
print(solution(grid, 0))
