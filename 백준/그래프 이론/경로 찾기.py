"""
시작 시간: 2022-10-21 02:52 PM
소요 시간: 20분
풀이 방법: 플로이드!
"""
# 입력
n = int(input())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)

# 플로이드
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

# 출력
for line in graph:
    for char in line:
        print(char, end = " ")
    print()
