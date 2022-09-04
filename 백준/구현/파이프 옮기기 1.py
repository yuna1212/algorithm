"""
시작 시간: 2022-09-04 PM 04:24
소요 시간: 2시간
풀이 방법:
    - DFS. 모든 경우를 탐색해야하므로 DFS, BFS 효율은 같다
    - 시간 초과..
"""
HORIZONTAL = '가로' 
VERTICAL = '세로' 
ACROSS = '대각선' 

INFO = {
    HORIZONTAL: { HORIZONTAL: [[0, 1]], ACROSS: [[1, 1], [0, 1], [1, 0]] },
    VERTICAL: { VERTICAL: [[1, 0]], ACROSS: [[1, 1], [0, 1], [1, 0]] },
    ACROSS: { HORIZONTAL: [[0, 1]], VERTICAL: [[1, 0]], ACROSS: [[1, 1], [0, 1], [1, 0]] }
}

def input_data():
    global N, MAP
    N = int(input())
    MAP = []
    for _ in range(N):
        line = input()
        row = []
        for char in line:
            if char != " ":
                row.append(char)
        MAP.append(row)

def input_file(path):
    global N, MAP
    fs = open(path, 'r')
    N = int(fs.readline().strip())
    MAP = []
    for _ in range(N):
        line = list(fs.readline().strip())
        row = []
        for char in line:
            if char != " ":
                row.append(char)
        MAP.append(row)

def is_movable(x, y, empty_diffs):
    global N, MAP
    for dx, dy in empty_diffs:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < N):
            return False 
        if MAP[nx][ny] != '0':
            return False
    return True 

global N, MAP
input_data()
stack = [(0, 1, HORIZONTAL)]
answer = 0
while stack:
    x, y, direction = stack.pop()
    if x == N-1 and y == N-1:
        answer+=1
        continue
    empties = INFO[direction]
    directions = empties.keys()
    for next_direction in directions:
        diffs = empties[next_direction]
        nx, ny = x+diffs[0][0], y+diffs[0][1]
        result = is_movable(x, y, diffs)
        if is_movable(x, y, diffs):
            stack.append((nx, ny, next_direction))
print(answer)



