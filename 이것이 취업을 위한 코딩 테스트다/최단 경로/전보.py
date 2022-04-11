"""
시작 시간: 2022년 4월 11일 오후 5시 50분
소요 시간: 20분
풀이 방법:
    다익스트라
"""
import heapq
n, m, c = map(int, input().split())
connection = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    connection[x].append((y, z)) # (연결 도시, 비용) 추가

queue = []
heapq.heappush(queue, (0, c)) # (도달 비용, 도시)

visited = set()
city_count, time_count = -1, 0
while queue:
    time, city = heapq.heappop(queue)
    if city in visited:
        continue
    visited.add(city)
    city_count += 1
    time_count = max(time_count, time)
    for next_city, addtional_costs in connection[city]:
        heapq.heappush(queue, (time+addtional_costs, next_city))
print(city_count, time_count)