"""
시작 시간: 2022-10-21 03:38 PM
소요 시간: 40분
풀이 방법: 다익스트라로 해결
"""
import sys
import heapq
input = sys.stdin.readline
INF = 10**6
def input_graph():
    n, m = map(int, input().strip().split()) # 집, 다리 수
    start, end = map(int, input().strip().split())
    graph = [[] for _ in range(n+1)] # graph[i] = (weight, j) i는 j와 weight만큼으로 연결
    for _ in range(m):
        i, j, weight = map(int, input().strip().split())
        graph[j].append((weight, i))
        graph[i].append((weight, j))
    return graph, start, end

def dkstr(graph, start, end):
    global INF
    visited = [False]*len(graph) 
    heap = [(-INF, start)]
    while heap:
        weight, node = heapq.heappop(heap)
        # 방문했다면 다음 루프
        if visited[node]: continue
        visited[node] = True
        weight = -weight

        # 목적지 도착했다면 리턴
        if node == end: return weight

        # 연결된 노드들을 힙에 넣기
        for next_weight, next_node in graph[node]:
            next_weight = min(weight, next_weight)
            heapq.heappush(heap, (-next_weight, next_node))
    
    return 0

graph, start, end = input_graph()
print(dkstr(graph, start, end))

