"""
시작 시간: 2022-10-18 03:08 PM
소요 시간: 1시간 30분
풀이 방법:
    - 2차원 배열을 1차원으로 표현할 때 인덱스 표현 주의(index = 열개수*x + y)
    - n, m을 바꿔쓰면서 계속 틀렸습니다.,,,,
"""

def get_safety_size(lab_map, viruses, walls):
    for x, y in walls:
        if lab_map[x][y] != 0: return -1
    for x, y in walls:
        lab_map[x][y] = 1
    
    visited = [ [False]*len(lab_map[0]) for _ in range(len(lab_map)) ]
    virus_stack = [] + viruses
    none_safety_size = 0
    diffs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    while virus_stack:
        x, y = virus_stack.pop()
        if not (0 <= x < len(lab_map) and 0 <= y < len(lab_map[0])):
            continue
        if visited[x][y]: continue
        visited[x][y] = True
        none_safety_size += 1
        if lab_map[x][y] == 1: continue
        for dx, dy in diffs:
            virus_stack.append([x+dx, y+dy])
    for x in range(len(lab_map)):
        for y in range(len(lab_map[0])):
            if visited[x][y]: continue
            if lab_map[x][y] == 0: continue
            none_safety_size += 1

    for x, y in walls:
        lab_map[x][y] = 0
    ans =  len(lab_map) * len(lab_map[0]) - none_safety_size 
    return ans

n, m = map(int, input().split())
lab_map = []
viruses = []
for x in range(n):
    line = list(map(int, input().split()))
    for y in range(m):
        if line[y] == 2:
            viruses.append([x, y])
    lab_map.append(line)

stack = []
for i in range(n):
    for j in range(m):
        stack.append([[i, j]])
max_safety_size = 0
while stack:
    walls = stack.pop()
    if len(walls) < 3:
        x, y = walls[-1]
        for next_pos in range(x*m+y+1, n*m):
            next_walls = list( wall for wall in walls )
            next_walls.append([next_pos // m, next_pos % m])
            stack.append(next_walls)
    else:
        max_safety_size = max(get_safety_size(lab_map, viruses, walls), max_safety_size)
print(max_safety_size)
