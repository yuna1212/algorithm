"""
시작 시간: 2023-02-17 02:10 AM
소요 시간: 20분
풀이 방법: BFS. visited 배열을 관리하기 때문에 주어진 문자열을 리스트로 안바꾸는게 더 좋을 것 같다
"""
from collections import deque

def get_cost(start, end):
    global MAP
    visited = [ [False]*len(MAP[0]) for _ in range(len(MAP)) ]
    diffs = ((-1, 0), (1, 0), (0, 1), (0, -1))
    queue = deque([(0, *start)])

    while queue:
        cost, x, y = queue.popleft()
        if (x, y) == end:
            return cost

        if not (0 <= x < len(MAP) and 0 <= y < len(MAP[0])) or visited[x][y] or MAP[x][y] == 'X': 
            continue

        cost += 1
        visited[x][y] = True

        for dx, dy in diffs:
            nx, ny = x + dx, y + dy
            queue.append((cost, nx, ny))

    return -1

def solution(maps):
    global MAP
    MAP = []
    start, lever, end = None, None, None

    for i, row in enumerate(maps):
        MAP.append(list(row))
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
            elif cell == "L":
                lever = (i, j)
            elif cell == "E":
                end = (i, j)

    lever_cost = get_cost(start, lever)
    if lever_cost < 0:
        return -1

    end_cost = get_cost(lever, end)
    if end_cost < 0:
        return -1
    
    return lever_cost + end_cost 

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
