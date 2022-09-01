"""
시작 시간: 2022-09-01 PM 02:25 
소요 시간: 2시간 
풀이 방법:
    퀸 위치를 저장한 stack을 관리하고, 브루트포스로 푼다.
    N이 9만 되어도 10초가까이 시간이 소요된다..
"""
def get_territory(position, queen_number):
    global BOARD, N
    ret = set() 
    # 가로, 세로 mark
    for i in range(N):
        if BOARD[position[0]][i] == queen_number:
            ret.add((position[0], i))
        if BOARD[i][position[1]] == queen_number:
            ret.add((i, position[1]))
    # 2, 4사분면을 가로지르는 대각선 mark
    x, y = position
    diff = min(x, y)
    x -= diff
    y -= diff
    while x < N and y < N:
        if BOARD[x][y] == queen_number:
            ret.add((x, y)) 
        x += 1
        y += 1
    # 1, 3사분면을 가로지르는 대각선 mark
    x, y = position
    diff = min(x, N-y-1)
    x -= diff
    y += diff
    while x < N and y >= 0:
        if BOARD[x][y] == queen_number:
            ret.add((x, y))
        x += 1
        y -= 1
    return ret
 
def is_inside(position):
    global N
    if position[0] < N and position[1] < N:
        return True
    return False

def mark(position, queen_number):
    global BOARD
    for (x, y) in get_territory(position, 0):
        BOARD[x][y] = queen_number

def unmark(position):
    global BOARD
    for (x, y) in get_territory(position, BOARD[position[0]][position[1]]):
        BOARD[x][y] = 0

def get_next(position):
    global BOARD, N
    x, y = position
    y += 1
    while x < N:
        while y < N:
            if BOARD[x][y] == 0:
                return x, y
            y += 1
        x += 1
        y = 0
    return x, y

N = 9 #int(input())
BOARD = [[ 0 for _ in range(N) ] for _ in range(N) ]
answer = 0
position = (0, 0)
queen_stack = []
while True:
    if is_inside(position):
        mark(position, len(queen_stack)+1)
        queen_stack.append(position)
        
        if len(queen_stack) == N:
            position = queen_stack.pop()
            unmark(position)
            answer += 1
        position = get_next(position)
    else:
        if queen_stack:
            position = queen_stack.pop()
            unmark(position)
            position = get_next(position)
        else:
            break 
print(answer)
