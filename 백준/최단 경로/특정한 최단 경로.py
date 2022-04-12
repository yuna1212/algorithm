"""
시작 시간: 2022년 4월 12일 오후 10시 5분
소요 시간: 30분
풀이 방법:
   틀렸다 함,, 
"""
import heapq
from sys import stdin
INF = 200000 * 1000 + 1

def dkstr(graph, start, end):
    costs = [INF for _ in range(len(graph) + 1)]
    queue = [(0, start)] # (비용, 노드)
    while queue:
        cost, node = heapq.heappop(queue)
        if node == end:
                return cost
        if costs[node] > cost:
            costs[node] = cost
            for c, n in graph[node]:
                queue.append((cost+c, n))
    return -1

def solution(graph, v1, v2, end):
    distance_v1_v2 = dkstr(graph, v1, v2)
    if distance_v1_v2 < 0:
        return -1

    candidates = []
    # start -> v1
    distance_start_v1 = dkstr(graph, 1, v1)
    if distance_start_v1 > 0:
        distance_v2_end = dkstr(graph, v2, end)
        if distance_v2_end < 0:
            return -1
        candidates.append(distance_start_v1 + distance_v1_v2 + distance_v2_end)
    # start -> v2
    distance_start_v2 = dkstr(graph, 1, v2)
    if distance_start_v2 > 0:
        distance_v1_end = dkstr(graph, v1, end)
        if distance_v1_end < 0:
            return candidates[0]
        candidates.append(distance_start_v2 + distance_v1_v2 + distance_v1_end)
    return min(candidates)

        

N, E = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, stdin.readline().split())
print(solution(graph, v1, v2, N))