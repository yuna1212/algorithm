"""
시작 시간: 2022-09-16 02:24 AM
소요 시간: 2시간 30분
풀이 방법:
    - BFS에 움직이는 말은 2개
    - 상하좌우를 dx dy로 나타내면 코드가 더 짧게 작성할 수 있다. 
        - move/tilt 함수는 방향을 나타내는 값만 다르고 구조는 동일하다.
"""
from collections import deque
RED, BLUE = 0, 1
def input_data():
    global BOARD, RED, BLUE, N, M, GOAL
    N, M = map(int, input().split())
    BOARD = []
    for i in range(N):
        line = list(input())
        BOARD.append(line)
        for j in range(M):
            if BOARD[i][j] == 'B':
                blue = (i, j)
                BOARD[i][j] = '.'
            elif BOARD[i][j] == 'R':
                red = (i, j)
                BOARD[i][j] = '.'
            elif BOARD[i][j] == 'O':
                GOAL = (i, j)
            else:
                continue
    return (red, blue)

def move_left(a_ball):
    global BOARD
    x, y = a_ball
    new_y = y
    while BOARD[x][new_y] == '.':
        new_y -= 1
    if BOARD[x][new_y] == 'O':
        return [x, new_y]
    return [x, new_y+1]

def move_right(a_ball):
    global BOARD
    x, y = a_ball
    new_y = y
    while BOARD[x][new_y] == '.':
        new_y += 1
    if BOARD[x][new_y] == 'O':
        return [x, new_y]
    return [x, new_y-1]

def move_upper(a_ball):
    global BOARD
    x, y = a_ball
    new_x = x
    while BOARD[new_x][y] == '.':
        new_x -= 1
    if BOARD[new_x][y] == 'O':
        return [new_x, y]
    return [new_x+1, y]
    
def move_down(a_ball):
    global BOARD
    x, y = a_ball
    new_x = x
    while BOARD[new_x][y] == '.':
        new_x += 1
    if BOARD[new_x][y] == 'O':
        return [new_x, y]
    return [new_x-1, y]

def arrived(a_ball):
    global GOAL
    if a_ball[0] == GOAL[0] and a_ball[1] == GOAL[1]: return True
    else: return False

def tilt_left(balls):
    global BOARD, RED, BLUE, GOAL
    next_red = move_left(balls[RED])
    next_blue = move_left(balls[BLUE])
    if next_red == next_blue and not arrived(next_red): 
        follower = next_red
        if balls[RED][1] < balls[BLUE][1]:
            follower = next_blue
        follower[1] += 1
    return (next_red, next_blue)

def tilt_right(balls):
    global BOARD
    next_red = move_right(balls[RED])
    next_blue = move_right(balls[BLUE])
    if next_red == next_blue and not arrived(next_red): 
        follower = next_red
        if balls[RED][1] > balls[BLUE][1]:
            follower = next_blue
        follower[1] -= 1
    return (next_red, next_blue)

def tilt_upper(balls):
    global BOARD
    next_red = move_upper(balls[RED])
    next_blue = move_upper(balls[BLUE])
    if next_red == next_blue and not arrived(next_red): 
        follower = next_red
        if balls[RED][0] < balls[BLUE][0]:
            follower = next_blue
        follower[0] += 1
    return (next_red, next_blue)

def tilt_down(balls):
    global BOARD
    next_red = move_down(balls[RED])
    next_blue = move_down(balls[BLUE])
    if next_red == next_blue and not arrived(next_red):
        follower = next_red
        if balls[RED][0] > balls[BLUE][0]:
            follower = next_blue
        follower[0] -= 1
    return (next_red, next_blue)

def check(visited, balls):
    global RED, BLUE, M
    red_x, red_y = balls[RED]
    blue_x, blue_y = balls[BLUE]
    x = red_x * M + red_y
    y = blue_x * M + blue_y
    if visited[x][y]:
        return False 
    else:
        visited[x][y] = True
        return True

origin_balls  = input_data()
visited = [ [False] * (N*M) for _ in range(N*M) ]
count = 1
queue = deque([(count, tilt_left(origin_balls)), (count, tilt_right(origin_balls)), (count, tilt_upper(origin_balls)), (count, tilt_down(origin_balls))])
answer = -1 
while queue:
    count, balls = queue.popleft()
    if count > 10 or arrived(balls[BLUE]):
        continue
    if balls[RED][0] == GOAL[0] and arrived(balls[RED]):
        answer = count 
        break
    if not check(visited, balls): 
        continue
    count += 1
    queue.append((count, tilt_left(balls)))
    queue.append((count, tilt_right(balls)))
    queue.append((count, tilt_upper(balls)))
    queue.append((count, tilt_down(balls)))
print(answer)
