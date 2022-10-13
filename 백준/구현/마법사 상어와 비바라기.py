"""
시작 시간: 2022-10-13 03:09 PM
소요 시간: 1시간 30분
풀이 방법:
    - 완전 구현 문제
    - 얼마나 논리적으로 작업을 나눌것인지
"""
from sys import stdin
input = stdin.readline
DIFFS = (None, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
CROSS_DIFFS = (DIFFS[2], DIFFS[4], DIFFS[6], DIFFS[8])
# input
def get_data():
    global N
    N, m = map(int, input().strip().split())
    area = []
    for _ in range(N):
        area.append(list(map(int, input().strip().split())))
    directions = []
    distances = []
    for _ in range(m):
        d, s = map(int, input().strip().split())
        directions.append(d)
        distances.append(s)
    return area, directions, distances

# 구름 옮기기
def move(cloud, direction, distance):
    global DIFFS, N
    dx, dy = DIFFS[direction][0]*distance, DIFFS[direction][1]*distance
    cloud_positions = []
    for i in range(N):
        for j in range(N):
            if cloud[i][j]: 
                cloud_positions.append((i, j))
                cloud[i][j] = False
    for x, y in cloud_positions:
        x = (x+dx) % N
        y = (y+dy) % N
        cloud[x][y] = True

# 비 내리기 + 물 복사 버그
def increase_water(cloud, area):
    global N, CROSS_DIFFS
    # 비내리기
    for x in range(N):
        for y in range(N):
            if cloud[x][y]:
                area[x][y] += 1
    # 물 복사 버그
    for x in range(N):
        for y in range(N):
            if not cloud[x][y]:
                continue
            for dx, dy in CROSS_DIFFS:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N:
                    if area[nx][ny] > 0:
                        area[x][y] += 1

def change(cloud):
    global N
    for x in range(N):
        for y in range(N):
            if cloud[x][y]:
                cloud[x][y] = False
            elif area[x][y] >= 2:
                cloud[x][y] = True
                area[x][y] -= 2

area, directions, distances = get_data()
cloud = [[False]*N for _ in range(N)]
cloud[N-1][0] = True; cloud[N-1][1] = True; cloud[N-2][0] = True; cloud[N-2][1] = True

for i in range(len(directions)):
    direction, distance = directions[i], distances[i]
    move(cloud, direction, distance)
    increase_water(cloud, area)
    change(cloud)

ans = 0
for line in area:
    ans += sum(line)
print(ans)
