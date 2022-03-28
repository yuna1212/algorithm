"""
시작 시간: 2022년 3월 28일 오후 1시
소요 시간: 20분
풀이 방법:
    모든 마을과 거리를 탐색 -> O(N)이지만, 2<=N<=1000이므로 주어진 시간 내 탐색 가능
"""
n = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = 0
min_cost = costs[0]
far_away = distances[0]
for i in range(1, n-1):
    if min_cost > costs[i]:
        result += far_away*min_cost
        min_cost = costs[i]
        far_away = distances[i]
    else:
        far_away += distances[i]
result += far_away*min_cost
print(result)