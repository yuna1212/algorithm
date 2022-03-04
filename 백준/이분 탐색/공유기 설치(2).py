"""
시작 시간: 2022년 3월 4일 오전 10시 30분
소요 시간: 50분
풀이 방법:
    라우터를 설치할 수 있는 거리를 전체 구간에서 이분탐색
    다만, 오른쪽 경계값이 탐색이 안될 수도 있음.. 
    그래서 마지막에 무조건 오른쪽 경계값도 가능한지 확인하는 분기문 넣었는데 좀더 우아하게 할 수 있는 방법..?
    -> 44~55줄을 31~41줄로 수정
    is_routable 메소드의 파라미터를 1부터 1씩 올려보면 결과는 특정 값(opt)를 경계로 왼쪽은 True, 오른쪽은 False를 리턴함
    찾는 답 opt는 True를 리턴하는 구간에서 가장 오른쪽 끝 값임
    따라서, 2개의 집에 대해 2개의 라우터를 설치하는 경우를 제외하고는 38줄의 반복문으로 opt를 찾을 수 있음
"""
from sys import stdin
def is_routable(router_distance):
    house_set_last_location = HOUSE_LOCATIONS[0]
    router_count = 1
    for house in HOUSE_LOCATIONS:
        if router_count >= C:
            return True
        if house - house_set_last_location >= router_distance:
            router_count += 1
            house_set_last_location = house
    if router_count >= C:
            return True
    return False
# 입력
n, C = map(int, stdin.readline().split())
HOUSE_LOCATIONS = []
for _ in range(n):
    HOUSE_LOCATIONS.append(int(input()))
HOUSE_LOCATIONS.sort()

# 탐색 - 최댓값을 찾아야 함
lo, hi = 1, HOUSE_LOCATIONS[-1] - HOUSE_LOCATIONS[0]
if is_routable(hi):
    print(hi)
else:    
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if is_routable(mid):
            lo = mid
        else:
            hi = mid
    print(lo)
    
# 탐색 - 최댓값을 찾아야 함
# lo, hi = 1, HOUSE_LOCATIONS[-1] - HOUSE_LOCATIONS[0]
# while hi - lo > 1:
#     mid = (hi + lo) // 2
#     if is_routable(mid):
#         lo = mid
#     else:
#         hi = mid
# if is_routable(hi):
#     print(hi)
# else:
#     print(lo)