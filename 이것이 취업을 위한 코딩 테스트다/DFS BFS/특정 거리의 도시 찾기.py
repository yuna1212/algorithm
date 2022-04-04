"""
시작 시간: 2022년 4월 4일 오후 3시 20분
소요 시간: 20분
풀이 방법:
    bfs
"""
from collections import deque
# 입력
n, m, k, x = map(int, input().split())
connections = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    connections[a].append(b)

queue = deque([(x, 0)])
visited = set()
result = False
while queue and result <= k:
    node, distance = queue.popleft()
    if distance == k and node not in visited:
        print(node)
        result += 1
    visited.add(node)
    distance += 1
    for next in connections[node]:
        if next not in visited:
            queue.append((next, distance))
if not result:
    print(-1)        