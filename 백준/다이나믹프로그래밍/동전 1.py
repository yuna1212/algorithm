"""
시작 시간: 2022-10-01 06:20 PM
소요 시간: 1시간 30분
풀이 방법:
    - 20분 보고 못풀어서 해설 확인
    - 테이블에 저장해 둔 결과에서, 동전의 가치만큼을 더해서 총 가치를 0부터 k까지 만든다.
"""
import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split())
coins = set()
for i in range(n):
    coins.add(int(input().strip()))

dp = [0]*(k+1)
for coin in coins:
    if coin > k: continue
    dp[coin] += 1
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
print(dp[k])    
