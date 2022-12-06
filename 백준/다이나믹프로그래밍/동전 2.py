"""
시작 시간: 2022-12-06 01:38 PM
소요 시간: 50분
풀이 방법: 잘 풀었었는데, continue, break의 분기문 제대로 처리 안해줘서 헤맸다. 분기문의 조건 꼼꼼하게 처리하기
"""
import sys
input = sys.stdin.readline
n, k = map(int, input().rstrip().split())
coins = set()

dp = [-1]*(k+1)
for _ in range(n):
    coin = int(input().rstrip())
    if coin > k: continue
    coins.add(coin)
    dp[coin] = 1

coins = sorted(list(coins))

for the_coin in range(1, k+1):
    for sub_coin in coins:
        if sub_coin > the_coin:
            break

        if dp[the_coin-sub_coin] < 0: 
            continue

        if dp[the_coin] < 0:
            dp[the_coin] = dp[sub_coin] + dp[the_coin - sub_coin]

        elif dp[the_coin] > dp[sub_coin] + dp[the_coin - sub_coin]:
            dp[the_coin] = dp[sub_coin] + dp[the_coin - sub_coin]
print(dp[k])
