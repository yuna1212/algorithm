"""
시작 시간: 2022-10-21 12:46 AM
소요 시간: 20분
풀이 방법: 풀이 참고해서 해결
"""
n = int(input())
numbers = list(map(int, input().split()))
cache = 0
ans = -1000
for number in numbers:
    if cache < 0:
        cache = number
    else:
        cache += number
    ans = max(ans, cache)
ans = max(ans, cache)
print(ans)
