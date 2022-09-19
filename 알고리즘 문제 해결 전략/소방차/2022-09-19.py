"""
시작 시간: 2022-09-19 07:13 PM
소요 시간: 50분
풀이 방법: 화재가 난 각각의 장소에서 다익스트라로 모든 장소까지의 최단거리 구한 뒤, 각 소방서 위치중 최소 최단거리 구하는 것을 찾아서 합함 -> 시간초과
"""
import heapq
PATH_MAX = 500*1000*100
def input_data():
    v, e, n, m = map(int, input().split()) # node 개수, edge 개수, 화재 개수, 소방서 개수
    graph = [ [] for _ in range(v+1) ]
    fire_stations = [] 
    fire_places = [] 
    for _ in range(e):
        a, b, t = map(int, input().split()) # 두 장소와 weight
        graph[a].append((b, t))
        graph[b].append((a, t))
    for node in map(int, input().split()):
        fire_places.append(node)
    for node in map(int, input().split()):
        fire_stations.append(node)
    return graph, fire_stations, fire_places

def solution():
    global PATH_MAX
    ret = 0
    graph, fire_stations, fire_places = input_data()
    for fire_place in fire_places:
        heap = [(fire_place, 0)]
        paths = [PATH_MAX]*len(graph)
        while heap:
            node, weight = heapq.heappop(heap)
            if weight >= paths[node]:  continue
            paths[node] = weight
            for next_node, next_weight in graph[node]:
                heapq.heappush(heap, (next_node, weight+next_weight))
        min_weight = paths[fire_stations[0]]
        for fire_station in fire_stations:
            min_weight = min(min_weight, paths[fire_station]) 
        ret += min_weight
    return ret

for _ in range(int(input())):
    print(solution())
