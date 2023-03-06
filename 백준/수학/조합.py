"""
시작 시간: 2023-03-07 03:15 AM
소요 시간: 10분
풀이 방법:
"""
n, m = map(int, input().split())
m = min(m, n-m)

result = 1
for _ in range(m):
    result *= n
    n -= 1

for i in range(1, m+1):
    result //= i

print(result)
