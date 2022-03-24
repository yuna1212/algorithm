"""
시작 시간: 2022년 3월 24일 오후 2시 5분
소요 시간: 20분
풀이 방법:
    그래프로 표현해보면서 보면 그리디하게 풀 수 있음
"""
# 입력
n = int(input())
coins = sorted(list(map(int, input().split())))

min_money = 1
for coin in coins:
    if min_money >= coin:
        min_money += coin
    else:
        break
print(min_money)