"""
시작 시간: 2022년 3월 28일 오후 10시 20분
소요 시간: 50분
풀이 방법:
    집과 치킨집에 대한 정보를 각각의 리스트에 저장
    집과 치킨집의 거리에 대해 2차원 리스트에 저장
    모든 치킨집에 대해 m개를 선택해봄으로써 최솟값 탐색 => nCr의 최대는 약 1700이고 총 2만개 언더이므로 시간복잡도도 괜찮음
"""
MAX = 2147483647
from itertools import combinations
def get_distance(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return abs(x) + abs(y)
n, m = map(int, input().split()) # n은 도시 크기, m은 남을 치킨집
houses = []
chickens = []
for i in range(n):
    data = tuple(map(int, input().split()))
    for j in range(n):
        space = data[j]
        if space == 1:
            houses.append((i, j))
        elif space == 2:
            chickens.append((i, j))

# 거리 구하기
distances = []
for i in range(len(houses)):
    line = []
    for j in range(len(chickens)):
        house, chicken = houses[i], chickens[j]
        line.append(get_distance(house, chicken))
    distances.append(line)
    
combs = combinations(range(len(chickens)), m)
min_sum_distance = MAX
for comb in combs:
    sum_distance = 0
    for house_idx in range(len(houses)):
        min_distance = MAX
        for j in range(len(comb)):
            chicken_idx = comb[j]
            min_distance = min(min_distance, distances[house_idx][chicken_idx])
        sum_distance += min_distance
    if min_sum_distance > sum_distance:
        min_sum_distance = sum_distance
print(min_sum_distance)
            