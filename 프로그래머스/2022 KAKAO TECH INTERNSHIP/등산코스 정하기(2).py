"""
시작 시간: 2022-09-22 01:53 AM
소요 시간: 1시간
풀이 방법:
    - 다익스트라
    - 문해전 최단 경로 알고리즘의 소방차 문제랑 풀이가 비슷하다.
    - 인접행렬로 그래프 표현할까 했는데 그러면 최악의경우 메모리 250MB.. 인접리스트로 표현하자
"""
import heapq
INF_WEIGHT = 10**7
def solution(n, paths, gates, summits):
    global INF_WEIGHT
    answer = []
    gates = set(gates)
    summits = set(summits)
    graph = [ [] for _ in range(n+1) ]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
    intensities = [INF_WEIGHT]*(n+1)
    heap = [ (0, summit, summit) for summit in summits ] # (intensity, 봉우리번호, 현재노드)
    ret_summit = n 
    ret_intensity = INF_WEIGHT
    while heap:
        intensity, summit, node = heapq.heappop(heap)
        if intensities[node] < intensity: 
            continue

        if node in gates: 
            if ret_intensity > intensity:
                ret_intensity = intensity
                ret_summit = summit
            elif ret_intensity == intensity:
                ret_summit = min(ret_summit, summit)
            intensities[node] = intensity
            continue

        if intensities[node] == intensity: continue
        intensities[node] = intensity
        for next_node, weight in graph[node]:
            heapq.heappush(heap, (max(weight, intensity), summit, next_node))

    return ret_summit, ret_intensity
