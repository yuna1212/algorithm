"""
시작 시간: 2022-10-21 01:08 AM
소요 시간: 50분
풀이 방법: 유일한 모양들 구분하고, 맨 뒤에 각 모양을 위치했을 때 경우의 수를 앞선 결과들 사용해서 구하기
"""
def solution():
    divisor=10007
    n = int(input())
    cache = [ 0, 1, 3 ]
    if n < 3: return cache[n]
    for i in range(3, n+1):
        cache.append((cache[i-1] + cache[i-2]*2%divisor)%divisor)
    return cache[-1]
print(solution())
