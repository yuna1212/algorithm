"""
시작 시간: 2022-11-16 02:53 AM
소요 시간: 20분
풀이 방법: O(NlogN)의 퀵소트 변형 알고리즘을 사용하는 기본 정렬 라이브러리 사용하기
"""
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = 0
swap_counting = 0
while swap_counting < k:
    if a[swap_counting] >= b[n-1-swap_counting]: break
    ans += b[n-1-swap_counting]
    swap_counting += 1
while swap_counting < n:
    ans += a[swap_counting]
    swap_counting += 1
print(ans)
