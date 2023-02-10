"""
시작 시간: 2023-02-10 09:48 AM
소요 시간: 1시간 20분
풀이 방법: BFS에서 단계별로 색 다르게 칠해야될 때, 큐 두번 나눠서 사용하는 것 주의
"""
from collections import deque
from sys import stdin
input = stdin.readline

NO_COLOR=0
RED=1
BLACK=2

def get_another(color):
    if color == RED:
        return BLACK
    return RED

def color_graph(vertex, color, graph, colors):
    """ BFS로, vertex를 시작으로 color 번갈아가면서 색칠하기 """
    queue = deque([vertex])

    while queue:
        next_queue = deque()
        for _ in range(len(queue)):
            vertex = queue.popleft()

            if colors[vertex] == NO_COLOR:
                colors[vertex] = color
                for next_vertex in graph[vertex]:
                    next_queue.append(next_vertex)

            elif colors[vertex] != color:
                return False

        color = get_another(color)
        queue = next_queue

    return True

def solution():
    # 그래프 만들기 
    num_of_vertices, num_of_edges = map(int, input().rstrip().split())
    graph = [ [] for _ in range(num_of_vertices + 1) ]
    for _ in range(num_of_edges):
        v1, v2 = map(int, input().rstrip().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    colors = [NO_COLOR]*(num_of_vertices + 1)

    # 색칠 안한 정점을 골라 그래프 색칠하기
    color = BLACK
    for i in range(1, num_of_vertices + 1):
        vertex_color = colors[i]
        if vertex_color != NO_COLOR:
            continue
        
        if not color_graph(i, color, graph, colors):
            return "NO"

    return "YES"

for _ in range(int(input().rstrip())):
    print(solution())
