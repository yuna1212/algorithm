"""
시작 시간: 2022-09-18 10:30 PM
소요 시간: 3시간
풀이 방법:
    - 재귀로 모든 경로 다 탐색 -> 시간초과
"""
import sys
sys.setrecursionlimit(100000)
TYPE_SHELTER, TYPE_GATE, TYPE_SUMMIT = 0, 1, 2

def dfs(node, summit, intensity):
    global VISITED_COUNT, NODES_TYPE, CONNECTION, TYPE_GATE, TYPE_SUMMIT, TYPE_SHELTER, START_NODE

    # 봉우리를 다녀왔고, 다시 출발점으로 돌아왔다면
    if summit is not None and node == START_NODE:
        return summit, intensity

    # 해당 노드를 필요 이상으로 방문하려고 하거나, 봉우리를 방문 했는데 또 봉우리를 방문하려고 하거나, 다른 출발점이면
    if VISITED_COUNT[node] > 2 \
        or (summit is not None and NODES_TYPE[node] == TYPE_SUMMIT)\
        or (NODES_TYPE[node] == TYPE_GATE and node != START_NODE):
        return None, None

    # 방문 마크
    VISITED_COUNT[node] += 1
    if NODES_TYPE[node] == TYPE_SUMMIT:
        summit = node
    
    final_summit, final_intensity = summit, intensity
    for (next_node, next_intensity) in CONNECTION[node]:
        result_summit, result_intensity = dfs(next_node, summit, next_intensity if intensity is None else max(intensity, next_intensity))
        if final_summit is None or (result_intensity is not None and final_intensity > result_intensity):
            final_intensity = result_intensity
            final_summit = result_summit
        elif final_intensity == result_intensity:
            final_summit = min(final_summit, result_summit)

    # 방문 마크 취소 후 리턴
    VISITED_COUNT[node] -= 1
    return final_summit, final_intensity

def solution(n, paths, gates, summits):
    global VISITED_COUNT, NODES_TYPE, CONNECTION, TYPE_GATE, TYPE_SUMMIT, TYPE_SHELTER, START_NODE
    CONNECTION = [ [] for _ in range(n+1) ]
    for (node1, node2, intensity) in paths:
        CONNECTION[node1].append((node2, intensity))
        CONNECTION[node2].append((node1, intensity))
    NODES_TYPE = [ TYPE_SHELTER ] * (n+1)
    VISITED_COUNT = [0] * (n+1)
    for gate in gates:
        NODES_TYPE[gate] = TYPE_GATE
    for summit in summits:
        NODES_TYPE[summit] = TYPE_SUMMIT

    summit, intensity = None, None
    for gate in gates:
        START_NODE = gate
        result_summit, result_intensity = dfs(START_NODE, None, None)

        if summit is None or intensity > result_intensity:
            intensity = result_intensity
            summit = result_summit
        elif intensity == result_intensity:
            final_summit = min(final_summit, result_summit)

    return summit, intensity 

