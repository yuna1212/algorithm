"""
시작 시간: 2022년 4월 12일 오후 5시 25분
소요 시간: 30분
풀이 방법:
    다익스트라
    visited를 따로 만들어서, 큐에 추가를 할 때 visit했는지 안했는지 검사했으나, 사실 그럴 필요가 없었음
    "방문"하여 비용을 업데이트했을 때에만 큐에 연결된 노드들을 추가하면 됨.
    "방문"하지 않게되면 노드를 추가하지 않으면 됨. --> 언젠가 큐는 비게 되기 때문에 무한루프x
    결론적으로 반복문 내에서 if문 한번만 쓰면 해결
"""
from sys import stdin
INF = 300000*10+1
import heapq
V, E = map(int, stdin.readline().split())
costs = [INF for _ in range(V+1)]
graph = [[] for _ in range(V+1)]
k = int(input())
for _ in range(E):
    x, y, z = map(int, stdin.readline().split())
    graph[x].append((z, y)) # (가중치, 목적지)

queue = [(0, k)] # (가중치, 목적지)

while queue:
    cost, destination = heapq.heappop(queue)
    if cost < costs[destination]:
        costs[destination] = cost # "방문"하여 최단경로 업데이트    
        for w, v in graph[destination]: # "방문"했다면, 그 다음 노드까지 가능성도 큐에 넣어서 나중에 검토
            heapq.heappush(queue,(w+cost, v))

for i in range(1, V+1):
    if costs[i] == INF:
        print("INF")
    else:
        print(costs[i])