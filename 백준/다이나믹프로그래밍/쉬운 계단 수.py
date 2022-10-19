"""
시작 시간: 2022-10-20 06:05 AM
소요 시간: 40분
풀이 방법: 0부터 9까지 각 개수를 저장하는 배열 재활용. 리턴 전 모듈러 연산 주의!
"""
n = int(input())
cache = [1]*10
cache[0] = 0

for _ in range(n-1):
    new_cache = [0] * 10
    new_cache[0] = cache[1]
    new_cache[9] = cache[8]
    for i in range(1, 9):
        new_cache[i] = (cache[i-1]+cache[i+1])%1000000000
    cache = new_cache
ans = 0
for element in cache:
    ans += element
    ans %= 1000000000
print(ans)
