"""
시작 시간: 2022-12-01 11:43 PM
소요 시간: 2시간 10분
풀이 방법: 키 에러
"""
import sys
input = sys.stdin.readline
N, k, r = map(int, input().rstrip().split())
ROADS = dict()
FARM = [[-1]*(N+1) for _ in range(N+1)]
DIFFS = ((-1, 0), (1, 0), (0, 1), (0, -1))

    
def union(cow1, cow2):
    global GROUP_OF, GROUP_HEIGHTS
    cow1 = find(cow1)
    cow2 = find(cow2)
    if cow1 == cow2: return

    if GROUP_HEIGHTS[cow1]< GROUP_HEIGHTS[cow2]:
        cow1, cow2 = cow2, cow1

    elif GROUP_HEIGHTS[cow1] == GROUP_HEIGHTS[cow2]:
        GROUP_HEIGHTS[cow1] += 1

    GROUP_OF[cow2] = cow1

def find(cow):
    global GROUP_OF
    if cow != GROUP_OF[cow]:
        GROUP_OF[cow] = find(cow)

    return GROUP_OF[cow]

def dfs(x, y, cow):
    global FARM, DIFFS
    cow = find(cow)
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if FARM[x][y] == -1:
            FARM[x][y] = cow
        elif find(FARM[x][y]) == find(cow):
            continue
        else:
            union(cow, FARM[x][y])
            continue

        for dx, dy in DIFFS:
            nx, ny = x + dx, y + dy
            if not ( 1 <= nx <= N and 1 <= ny <= N) or ((x, y) in ROADS and (nx, ny) in ROADS[(x, y)]):
                continue
            stack.append((nx, ny))
    
for _ in range(r):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    if (x1, y1) in ROADS:
        ROADS[(x1, y1)].add((x2, y2))
        ROADS[(x2, y2)].add((x1, y1))
    else:
        ROADS[(x1, y1)] = set([(x2, y2)])
        ROADS[(x2, y2)] = set([(x1, y1)])

cows_positions = []
for i in range(k):
    x, y = map(int, input().rstrip().split())
    cows_positions.append((x, y))

GROUP_OF = [i for i in range(k)]
GROUP_HEIGHTS = [1]*k

for i, (x, y) in enumerate(cows_positions):
    dfs(x, y, i)

counter = dict()
for group in GROUP_OF:
    if group in counter: counter[group] += 1
    else: counter[group] = 1

counter = list(counter.values())
ans = 0
for i in range(len(counter)):
    summing = 0
    for j in range(i+1, len(counter)):
        summing += counter[j]
    ans += summing * counter[i]
print(ans)
