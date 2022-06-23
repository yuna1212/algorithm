"""
시작 시간: 2022년 6월 23일 오후 5시 5분
소요 시간: 50분
풀이 방법: usado를 어떻게 계산하는지 유의하기. 그 외에는 평범한 BFS 문제
"""
from sys import stdin
def answer(k, v):
    global GRAPH, N
    visited = [False] * (N+1)
    counter = 0
    stack = []
    
    for vertex_info in GRAPH[v]: stack.append(vertex_info)
    visited[v] = True
    while stack:
        v, usado = stack.pop()
        if visited[v] or usado < k:
            continue
        visited[v] = True
        counter += 1
        for other_v, other_usado in GRAPH[v]: stack.append((other_v, min(other_usado, usado)))
        
    return counter


global N, GRAPH
N, q = map(int, input().split())
GRAPH = [[] for _ in range(N+1)] # graph[i] = (p, usado), i노드는 q와 연결되어있고 가중치는 usado이다.
for _ in range(N-1):
    vertex, other_vertex, usado = map(int, stdin.readline().split())
    GRAPH[vertex].append((other_vertex, usado))
    GRAPH[other_vertex].append((vertex, usado))
for _ in range(q):
    k, v = map(int, stdin.readline().split())
    print(answer(k, v))