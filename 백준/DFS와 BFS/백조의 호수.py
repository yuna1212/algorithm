"""
시작 시간: 2022-10-21 09:10 PM
소요 시간: 1시간 40분
풀이 방법: union find 써서 풀었으나 시간초과
"""
import sys
input = sys.stdin.readline
def union(u, v):
    global PARENT_OF, RANK
    # u, v의 루트 찾기
    u = find(u)
    v = find(v)
    
    # 부모가 같다면 합칠 필요 없음
    if u == v: return

    # 깊이가 깊은게 u, 깊은게 낮은걸 포함
    if RANK[u] > RANK[v]:
        u, v = v, u
    PARENT_OF[v] = u

    # 깊이가 같았다면 u의 깊이를 1만큼 늘림
    if RANK[u] == RANK[v]:
        RANK[u] += 1
    return

def find(u):
    global PARENT_OF
    while u != PARENT_OF[u]:
        u = PARENT_OF[u]
    return u

def input_data():
    graph = []
    position_of_swans = []
    r, c = map(int, input().strip().split())
    for x in range(r):
        line = list(input().strip())
        for y in range(c):
            if line[y] == 'L':
                position_of_swans.append((x, y))
                line[y] = '.'
        graph.append(line)
    return graph, position_of_swans 

def is_valid(height, width, point):
    x, y = point
    if 0 <= x < height and 0 <= y < width:
        return True
    return False

def mark(graph, point, marking_index):
    stack = [point]
    diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while stack:
        x, y = stack.pop()
        # 검증
        if not is_valid(len(graph), len(graph[0]), (x, y)):
            continue
        if graph[x][y] != '.': continue 
            
        graph[x][y] = marking_index
        for dx, dy in diff:
            stack.append((x+dx, y+dy))

def get_adjacent_water_index(graph, point):
    global PARENT_OF
    x, y = point
    diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for dx, dy in diff:
        nx, ny = x+dx, y+dy
        if not is_valid(len(graph), len(graph[0]), (nx, ny)):
            continue
        if graph[nx][ny] != 'X':
            return graph[nx][ny]
    return None

def melt_day(graph):
    melting_points = [] # melting_points[i] = [[x, y], set(0, 2, 3)]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 'X':
                adjacent_water_index = get_adjacent_water_index(graph, (i, j))
                if adjacent_water_index is not None:
                    melting_points.append(((i, j), adjacent_water_index))
    for point, water_index in melting_points:
        x, y = point
        graph[x][y] = water_index

    diff = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for point, _ in melting_points:
        x, y = point
        for dx, dy in diff:
            nx, ny = x+dx, y+dy
            if is_valid(len(graph), len(graph[0]), (nx, ny)) and graph[nx][ny] != 'X':
                union(graph[x][y], graph[nx][ny])

# 데이터 초기화
graph, swans = input_data()
water_index = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == '.':
            mark(graph, (i, j), water_index)
            water_index += 1
PARENT_OF = [ i for i in range(water_index) ]
RANK = [0]*water_index

swans_groups = [ graph[x][y] for x, y in swans ]
day = 0
while find(swans_groups[0]) != find(swans_groups[1]):
    melt_day(graph)
    day += 1
print(day)

