"""
시작 시간: 2022-11-27 01:18 PM
소요 시간: 1시간
풀이 방법: 현실의 사물을 컴퓨터에서 어떻게 효과적으로 생각할 것인가를 고민하는게 중요했음
    - 변수 8개 사용했지만 변수 6개만 사용해서 주사위 표현해도 충분,,,
    - 동, 서, 남, 북마다 값만 각각 바꿔주면 되니까
"""
from collections import deque
DICE_HORIZONTAL = deque([0, 0, 0, 0])
DICE_VERTICAL = deque([0, 0, 0, 0])
BOARD = []

def synch_from_horizontal():
    DICE_VERTICAL[0] = DICE_HORIZONTAL[0]
    DICE_VERTICAL[2] = DICE_HORIZONTAL[2]
    
def synch_from_vertical():
    DICE_HORIZONTAL[0] = DICE_VERTICAL[0]
    DICE_HORIZONTAL[2] = DICE_VERTICAL[2]
    
def turn_east():
    DICE_HORIZONTAL.appendleft(DICE_HORIZONTAL.pop())
    synch_from_horizontal()

def turn_west():
    DICE_HORIZONTAL.append(DICE_HORIZONTAL.popleft())
    synch_from_horizontal()

def turn_north():
    DICE_VERTICAL.appendleft(DICE_VERTICAL.pop())
    synch_from_vertical()

def turn_south():
    DICE_VERTICAL.append(DICE_VERTICAL.popleft())
    synch_from_vertical()

def copy_at(x, y):
    board_number = BOARD[x][y]
    dice_bottom_number = DICE_HORIZONTAL[2]
    if board_number == 0:
        BOARD[x][y] = dice_bottom_number
    else:
        BOARD[x][y] = 0
        DICE_HORIZONTAL[2] = DICE_VERTICAL[2] = board_number


n, m, x, y, k = map(int, input().split()) # 세로, 가로, 주사위 x, 주사위 y, 명령 개수
for _ in range(n):
    BOARD.append(list(map(int, input().split())))

directions = tuple(map(int, input().split()))
turns = (None, turn_east, turn_west, turn_north, turn_south)
diffs = (None, (0, 1), (0, -1), (-1, 0), (1, 0))
for direction in directions:
    dx, dy = diffs[direction]
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x, y = nx, ny
    turns[direction]()
    copy_at(x, y)
    print(DICE_HORIZONTAL[0])

