"""
시작 시간: 2022년 4월 8일 오후 3시 15분
소요 시간: 20분
풀이 방법:
    다익스트라 말고 BFS로 풀었다. 
    어차피 거리가 모두 1이니, BFS로 푸는게 시간도 덜걸림
"""
from collections import deque
from time import time
def get_distance(graph, start, destination):
    queue = deque([(start, 0)])
    visited = set()
    while queue:
        here, distance = queue.popleft()
        if here == destination:
            return distance
        if here not in visited:
            visited.add(here)
            for next in graph[here]:
                queue.append((next, distance + 1))
    return -1
###################### BFS 풀이
# 입력
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
x, k = map(int, input().split())

# 출력
start_time = time()
meetting_distance = get_distance(graph, 1, k)
if meetting_distance > -1:
    dating_distance = get_distance(graph, 1, x)
    if dating_distance > -1:
        print(meetting_distance + dating_distance)
    else:
        print(-1)
else:
    print(-1)
end_time = time()
print(f"BFS로 풀었을 때 시간: {end_time-start_time}")
###################### 플로이드 워셜
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 X와 최종 목적지 노드 K를 입력받기
x, k = map(int, input().split())

start_time = time()
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우, -1을 출력
if distance >= 1e9:
    print("-1")
# 도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)
end_time = time()
print(f"플로이드 워셜로 풀었을 때 시간: {end_time-start_time}")