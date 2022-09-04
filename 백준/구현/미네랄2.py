"""
시작 시간: 2022-09-04 AM 11:19
소요 시간: 1시간 30분
풀이 방법:
    - 클러스터 번호에 대해, 클러스터 크기와 하나의 좌표를 저장하는 dictionary 선언
    - 클러스터를 얼마나 이동할 수 있는지 탐색하기
    - 해결x...
"""
def input_file(path):
    f = open(path, 'r')
    global MAP
    MAP = []
    r, c = map(int, f.readline().split())
    for _ in range(r):
        MAP.append(list(f.readline().strip()))
    
def input_data():
    global MAP
    MAP = []
    r, c = map(int, input().split())
    for _ in range(r):
        MAP.append(list(input()))

def print_cave():
    global MAP
    for line in MAP:
        for char in line:
            print(char, end="")
        print()

def cluster(position):
    global MAP, NEXT_CLUSTER_ID, CLUSTER
    if MAP[position[0]][position[1]] == ".": return
    count = 0
    diffs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    id = NEXT_CLUSTER_ID
    NEXT_CLUSTER_ID += 1
    CLUSTER[id]= [0, position] # 크기, 위치
    stack = [position]
    while stack:
        x, y = stack.pop()
        if not ( 0 <= x < len(MAP) and 0 <= y < len(MAP[0])):
            continue
        if MAP[x][y] == "." or MAP[x][y] == id: 
            continue
        MAP[x][y] = id
        count += 1
        for dx, dy in diffs:
            stack.append((x+dx, y+dy))
    CLUSTER[id][0] = count

def move(cluster_id, step):
    global MAP, CLUSTER
    diffs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    x, y = CLUSTER[cluster_id][1]
    stack = [(x, y)]
    positions = []

    while stack:
        x, y = stack.pop()
        if not ( 0 <= x < len(MAP) and 0 <= y < len(MAP[0])):
            continue
        if MAP[x][y] != cluster_id: 
            continue

        MAP[x][y] = "." 
        positions.append((x, y))
        for dx, dy in diffs:
            stack.append((x+dx, y+dy))
            
    for x, y in positions:
        MAP[x+step][y] = cluster_id

def find_movable_step(cluster_id):
    global MAP, CLUSTER
    diffs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    x, y = CLUSTER[cluster_id][1]
    stack = [(x, y)]
    min_step = len(MAP) - x
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue
        if not ( 0 <= x < len(MAP) and 0 <= y < len(MAP[0])):
            continue
        if MAP[x][y] != cluster_id:
            continue
        if x+1 < len(MAP) and MAP[x+1][y] == cluster_id:
            continue
        for i in range(min_step):
            if x+min_step >= len(MAP):
                min_step = i-1
                print(min_step)
                break
            next_symbol = MAP[x+min_step][y]
            if next_symbol != cluster_id or next_symbol != ".":
                min_step = i-1
                print(min_step)
                break
        visited.add((x, y))
        for dx, dy in diffs:
            stack.append((x+dx, y+dy))
    return min_step

NEXT_CLUSTER_ID = 0
CLUSTER = {}
# input_data()
input_file(input())
cluster((1, 2))
print_cave()
print(find_movable_step(0))
move(0, 1)
print_cave()
