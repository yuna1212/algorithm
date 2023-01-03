"""
시작 시간: 2023-01-03 11:56 PM
소요 시간: 20분
풀이 방법:
"""
n = int(input())
memo = [0, 1]

for i in range(n):
    ans = sum(memo) % 10007
    memo[0], memo[1] = memo[1], ans

print(ans)
