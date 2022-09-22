"""
시작 시간: 2022-09-22 10:24 PM
소요 시간: 2시간
풀이 방법:
    - 전체 시간 복잡도: O(N^3)
        - 플로이드: O(N^3)
        - 음주 측정: O(N)
    - 책과 같은 풀이
    - 변수 이름 다르게 써서 시간 많이 버렸다,,
    - 음주 측정할 노드를 k, 출발지를 i, 도착지를 j라고 하자
        - i -> k, k -> j는 각각 최단경로를 가져야 한다.
        - 각 최단 경로에 k에서 음주 측정할 때 걸리는 시간만 더해주면 된다.
    - 모든 경로를 다 봐야한다.
        - 경로를 기준으로 보지 말고, 음주 측정할 '노드'를 기준으로 본다.
        - 모든 경유점에 대해 탐색
"""
INF = 101
# 데이터 입력
v, e = map(int, input().split()) # 장소 수, 도로 수
cost = None
graph =  [ [INF]*(v+1) for _ in range(v+1) ]
cost = tuple(map(int, input().split()))
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# 플로이드-워셜
for i in range(v+1): graph[i][i] = 0
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 테스트케이스만큼 답 찾기
for _ in range(int(input())):
    s, t = map(int, input().split())
    # 음주단속시 최소 경로 찾기
    result = INF*e+INF
    for k in range(v):
        if k == s or k == t: continue
        result = min(result, graph[s][k] + graph[k][t] + cost[k])
    print('>>', result)
