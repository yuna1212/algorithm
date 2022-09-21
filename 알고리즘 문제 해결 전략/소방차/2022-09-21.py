"""
시작 시간: 2022-09-21 08:58 PM
소요 시간: 1시간 30분
풀이 방법:
    - 소방서부터 시작한다.
    - 시작지점을 힙에 넣을 때 여러 개를 넣는다. 소방서 자기 자신까지의 거리는 0
    - 이후에 다익스트라.
    - 소방서 리스트와 화재 장소 리스트를 따로 관리한다.
"""
import heapq
INF = 500000
def input_data():
    global TYPE_STATION, TYPE_FIRED, INF
    v, e, m, n = map(int, input().split()) # 장소, 도로, 화재 장소, 소방서 수
    graph = [ [0]*(v+1) for _ in range(v+1) ]
    for _ in range(e):
        a, b, t = map(int, input().split())
        graph[a][b] = t
        graph[b][a] = t
    fire_places = []
    fire_stations = []
    for p in map(int, input().split()):
        fire_places.append(p)
    for p in map(int, input().split()):
        fire_stations.append(p)
    return graph, fire_places, fire_stations  

def solution():
    global INF
    graph, fire_places, fire_stations = input_data()
    time_table = [INF]*len(graph)
    heap = [(0, p) for p in fire_stations]
    heapq.heapify(heap)
    while heap:
        time, place = heapq.heappop(heap)
        if time >= time_table[place]: continue
        time_table[place] = time
        for i in range(len(graph)):
            if graph[place][i] == 0: continue
            heapq.heappush(heap, (time+graph[place][i], i))
    ret = 0
    for p in fire_places:
        ret += time_table[p]
    return ret

t = int(input())
for _ in range(t):
    print(solution())
