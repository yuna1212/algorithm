"""
시작 시간: 2022년 4월 15일 오전 11시 10분
소요 시간: 30분
풀이 방법:
    fish 위치를 찾고, 거기까지 경로를 다시 찾는 것이 문제인듯. 중복적으로 스캔하기 때문에
    단순 BFS로 했는데, 위, 왼쪽, 오른쪽, 아래 순서를 맞춰주기 위해서는
    최소의 거리에 있는 모든 점을 저장한다음 위, 왼쪽, 오른쪽, 아래 우선순위대로 최우선값 뽑아내야 함
"""
FISH_INF_SIZE = 7
from sys import stdin
from collections import deque
def bfs(grid_map, start, size):
    visited = [[False for _ in range(len(grid_map))] for _ in range(len(grid_map))]
    candidates = deque([(0, start)]) # (걸린 시간, (x, y))
    movings = [(-1, 0), (0, -1), (0, 1), (1, 0)] # 위, 왼쪽, 오른쪽, 아래
    min_cost = 400
    closest_fishes = []
    while candidates:
        cost_time, (x, y) = candidates.popleft()
        if visited[x][y]:
            continue
        if cost_time > min_cost:
            break
        if 0 < grid_map[x][y] < size: # 먹을 수 있음
            min_cost = cost_time
            closest_fishes.append((x, y))
        if grid_map[x][y] <= size: # 지나갈 수 있음
            cost_time += 1
            visited[x][y] = True
            for dx, dy in movings:
                nx, ny = x+dx, y+dy
                if 0<=nx<len(grid_map) and 0<=ny<len(grid_map):
                    candidates.append((cost_time, (nx, ny)))
    
    if closest_fishes:
        eatable_fish = min(closest_fishes)
        return min_cost, eatable_fish
    return 
            
        
    

def solution():
    # 데이터 입력
    n = int(input())
    grid_map = []
    x, y = -1, -1
    for i in range(n):
        line = list(map(int, stdin.readline().split()))
        grid_map.append(line)
        if 9 in line:
            x, y = i, line.index(9)
            grid_map[x][y] = 0
    
    # 몇 초 견딜 수 있는지 구하기
    cost = 0
    baby_size = 2
    ate_count = 0
    while True:
        next_info = bfs(grid_map, (x, y), baby_size)
        if next_info:
            cost_time, (fish_x, fish_y) = next_info
            cost += cost_time
            ate_count += 1
            if ate_count == baby_size:
                baby_size += 1
                ate_count = 0
            x, y = fish_x, fish_y
            grid_map[x][y] = 9
            grid_map[x][y] = 0
        else:
            return cost

print(solution())