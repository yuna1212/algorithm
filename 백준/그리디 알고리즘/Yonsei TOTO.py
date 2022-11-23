"""
시작 시간: 2022-11-23 09:25 PM
소요 시간: 40분
풀이 방법: 
    - 정렬 문제
    - 전체를 다 정렬할 필요가 없어 선택정렬을 구현했으나, 오히려 느려졌다.
    - 내부적으로 O(NlogN)으로 구현되어있으나, N을 줄이는 대신 O(N^2)으로 구현한 것과 큰 차이 없는듯
    - 퀵정렬을 변형하면 더 빨라질지도?
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split()) # 과목 수, 마일리지
min_miles = []
for _ in range(n):
    p, l = map(int, input().strip().split()) # 신청수, 수강인원
    miles = list(map(int, input().strip().split()))

    if p < l:
        min_miles.append(1)
    else:
        for i in range(l):
            for j in range(i+1, p):
                if miles[i] < miles[j]:
                    miles[i], miles[j] = miles[j], miles[i]
        min_miles.append(miles[l-1])

min_miles.sort()

ans = 0
for mile in min_miles:
    if m - mile >= 0:
        ans += 1
        m -= mile
    else:
        break
print(ans)
