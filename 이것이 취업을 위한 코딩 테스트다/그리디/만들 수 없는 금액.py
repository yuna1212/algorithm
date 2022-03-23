"""
시작 시간: 2022년 3월 23일 오후 12시
소요 시간: 1시간
풀이 방법:
    모든 조합 만들어서 풀어보긴 했지만, 그리디하게 푸는 방법은 조금 생소하다..
"""
from itertools import combinations
# 입력
n = int(input())
coins = sorted(list(map(int, input().split())))

# solution 1: 생각나는대로..
impossible_min = 1
r = 1
while r < n + 1:
    combination = combinations(coins, r)
    for comb in combination:
        # made로 금액 만들기
        made = 0
        for coin in comb:
            made += coin
            
        # 만든 금액이 불가능했든 금액과 같다면
        if made == impossible_min:
            impossible_min += 1
            r = 1
            break
    r += 1
print(impossible_min)

# solution 2: 좀 더 그리디하게
# 최솟값 이전의 값들은 모두 만들어봤고, 그 이후에 만들 수 있는 값은 무엇인가?
impossible_min = 1
for coin in coins:
    if impossible_min < coin:
        break
    impossible_min += coin
print(impossible_min)