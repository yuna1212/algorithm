"""
시작 시간: 2022년 3월 10일 오후 1시
소요 시간: 1시간
풀이 방법:
    단순한 DFS, BFS 구현 문제
    이미 방문한 정점은 다시 방문하지 않는 조건을 달아 구현했다.
    
    "어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다"라는 조건을 잘못 해석함
    두 정점을 곧장 연결하는 간선은 둘 이상일 수 있다, 여러 번 정점을 방문할 수 있다로 해석함
    그래서 BFS, DFS가 그래프 간선 개수를 수정하기에 동일 그래프를 두번 저장했지만,
    해당 조건은 신경쓰지 말고 진행했어도 될일
"""
from sys import stdin

""" 데이터 입력받기 """
n, m, v = map(int, stdin.readline().split())
# 인접행렬 전역 선언, 그래프 만들기
GRAPH = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, input().split())
    GRAPH[node1][node2] += 1
    GRAPH[node2][node1] += 1
    
# DFS, BFS 결과 저장 변수
DFS_RESULT = []
BFS_RESULT = []

""" DFS 구현 """
def dfs(start):
    global DFS_RESULT, GRAPH
    DFS_RESULT.append(start)
    for i in range(1, len(GRAPH)):
        if GRAPH[start][i] > 0 and i not in DFS_RESULT:
            # i에서 다시 탐색
            dfs(i)

# BFS 구현
def bfs(start):
    global BFS_RESULT, GRAPH
    will_visit = [start]
    while will_visit:
        visitting = will_visit.pop(0)
        BFS_RESULT.append(visitting)
        for i in range(len(GRAPH)):
            if GRAPH[visitting][i] > 0 and i not in will_visit and i not in BFS_RESULT:
                will_visit.append(i)

""" 실행 """
dfs(v)
for element in DFS_RESULT:
    print(element, end=" ")
print()    
bfs(v)
for element in BFS_RESULT:
    print(element, end=" ")