"""
시작 시간: 2022년 4월 20일 오후 3시 40분
소요 시간: 1시간 30분
풀이 방법:
    결과가 무조건 -1이 나옴
    가장 가까운 출발지를 찾지 못하고있다.
    
    출발지를 번호를 2부터 쭉 붙여서 area에 빈칸과 벽과 함께 표시했는데
    다른 방법을 찾는게 좋을 것 같다.
"""
from sys import stdin
from collections import deque
INF = 401
def get_passenger_distance_position(area, x, y):
    visited = [[False for _ in range(len(area))] for _ in range(len(area))]
    min_distance = INF
    queue = deque([(0, x, y)])
    min_distances = []
    moving = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while queue:
        distance, x, y = queue.pop()
        
        if area[x][y] == 1 or visited[x][y]:
            continue
        
        visited[x][y] = True
        
        if distance > min_distance:
            break
        
        if area[x][y] > 1 and distance <= min_distance:
            min_distances.append((distance, x, y))
        else:
            distance += 1
            for dx, dy in moving:
                nx, ny = x+dx, y+dy
                if 0<=nx<len(area) and 0<=ny<len(area):
                    queue.append((distance, nx, ny))
        
    if len(min_distances) > 0:
        return min(min_distances, key=lambda x: (x[1], x[2]))
    return 

def get_target_position_distance(area, x, y, target_x, target_y):
    distance = 0
    visited = [[False for _ in range(len(area))] for _ in range(len(area))]
    moving = [(0, 1), (1, 0), (-1, 0), (0, -1)]
   
    queue = deque([(0, x, y)])
    while queue:
        distance, x, y = queue.pop()
        if (x, y) == (target_x, target_y):
            return distance
        if visited[x][y]:
            continue
        visited[x][y] = True
        distance += 1
        for dx, dy in moving:
            nx, ny = x+dx, y+dy
            if 0<=nx<len(area) and 0<=ny<len(area):
                queue.append((distance, nx, ny))
    
    return
# 입력
n, m, fuel = map(int, stdin.readline().split())
area = [[1 for _ in range(n+1)]]
for _ in range(n):
    line = [1] + list(map(int, stdin.readline().split()))
    area.append(line)
x, y = map(int, stdin.readline().split())
targets = [0 for _ in range(2+m)]
for i in range(2, 2+m):
    sx, sy, tx, ty = map(int, stdin.readline().split())
    area[sx][sy] = i
    targets[i] = (tx, ty)

for _ in range(m):
    passenger_info = get_passenger_distance_position(area, x, y)
    if passenger_info:
        distance, px, py = passenger_info
        if fuel >= distance:
            # 출발지 이동
            fuel -= distance
            x, y = px, py
            tx, ty = targets[area[px][py]]
            area[px][py] = 0
            
            distance = get_target_position_distance(area, x, y, tx, ty)
            if fuel >= distance:
                # 도착지 이동
                x, y = tx, ty
                fuel -= distance
            else:
                fuel = -1
                break
            
        else:
            fuel = -1
            break
    else:
        fuel = -1
        break
        
print(fuel)