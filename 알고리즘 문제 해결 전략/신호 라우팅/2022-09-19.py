"""
시작 시간: 2022-09-19 06:31 PM
소요 시간: 30분
풀이 방법: 전형적인 다익스트라
"""
INF_NOISE = 4*20000
import heapq
def input_data():
    n, m = map(int, input().split())
    connections = [ [] for _ in range(n) ]
    for _ in range(m):
        computer1, computer2, noise = input().split()
        computer1, computer2 = int(computer1), int(computer2)
        noise = float(noise)
        connections[computer1].append((computer2, noise))
        connections[computer2].append((computer1, noise))
    return connections

def solution():
    global INF_NOISE
    heap = []
    for _ in range(int(input())):
        connections = input_data()
        noises = [INF_NOISE]*len(connections) 
        heapq.heappush(heap, (0, 1)) # (노드 번호, 해당 노드까지 최단 경로)
        while heap:
            node, noise = heapq.heappop(heap)
            if noise >= noises[node]: continue
            noises[node] = noise 
            for (next_node, next_noise) in connections[node]:
                heapq.heappush(heap, (next_node, noise*next_noise))
        print(noises[len(noises)-1])

solution()
