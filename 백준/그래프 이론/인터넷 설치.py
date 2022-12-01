"""
시작 시간: 2022-12-01 09:51 PM
소요 시간: 1시간
풀이 방법: 다익스트라, 메모리 초과..!, visited 사용 없이 경로를 각 경우마다 모두 저장해서 그런듯
"""
import sys, heapq
input = sys.stdin.readline
n, p, k = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)] # graph[i] = (node, cost) 
for _ in range(p):
    com1, com2, cost = map(int, input().rstrip().split())
    graph[com1].append((com2, cost))
    graph[com2].append((com1, cost))

heap = [(0, [], 1, 0)] # 지불해야 할 값, 공짜 케이블들, 위치, 사용한 케이블 개수
ans = -1
while heap:
    fee, free_cables, node, cable_counter = heapq.heappop(heap)
    if cable_counter > p: 
        continue 

    if node == n:
        if ans == -1: ans = fee
        else: ans = min(ans, fee)
        continue

    cable_counter += 1 

    for next_node, cost in graph[node]:
        next_free_cables = free_cables[:]
        heapq.heappush(next_free_cables, cost)
        if len(next_free_cables) > k:
            extra_cable_cost = heapq.heappop(next_free_cables)
            fee = max(fee, extra_cable_cost)
        heapq.heappush(heap, (fee, next_free_cables, next_node, cable_counter))

print(ans)

