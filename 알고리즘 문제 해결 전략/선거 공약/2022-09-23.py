"""
시작 시간: 2022-09-23 01:42 AM
소요 시간: 40분
풀이 방법:
    - 간선 새로 update시 해당 간선을 포함할 수도 있는 다른 경로들도 검토해야하는 부분에서 살짝 버벅이긴 했는데 문제없었다.
        - 처음에 a와 b를 연결하는 간선의 update를, a -> b -> ?와 b -> a -> ?로 일부만 처리해버림.
            - 주어진 테케에서만 문제 없음
        - 간선 변경 = 간선으로 연결되는 노드의 변경 = 해당 노드를 거치는 다른 경로의 변경
"""
INF = 101
c = int(input())
for _ in range(c):
    v, m, n = map(int, input().split()) # 도시 수, 고속도로 수, 건설될 도로 수
    graph = [ [INF]*v for _ in range(v) ]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    additive_connection = [] # (도시, 도시, 이동시간)
    for _ in range(n):
        additive_connection.append(tuple(map(int, input().split())))

    # 플로이드
    for k in range(v):
        graph[k][k] = 0
        for i in range(v):
            if graph[i][k] == INF: continue
            for j in range(i+1, v):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                graph[j][i] = graph[i][j]

    # 새로 추가할 연결과 비교
    ret = 0
    for a, b, c in additive_connection:
        if graph[a][b] <= c: ret += 1
        else:
            # 변경된다면 간선을 포함할 다른 경로들도 업데이트 해줘야한다.
            graph[a][b] = c
            graph[b][a] = c
            for src in range(v):
                for dest in range(src+1, v):
                    graph[src][dest] = min(graph[src][dest],\
                                            min(graph[src][a] + graph[a][b] + graph[b][dest], graph[src][b] + graph[b][a] + graph[a][dest]))
                    graph[dest][src] = graph[src][dest]

    print('>>', ret)
