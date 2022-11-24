"""
시작 시간: 2022-11-24 08:52 PM
소요 시간: 30분
풀이 방법: O(nk) -> 시간 초과
"""
import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split()) # 보석 개수, 가방 개수
jewelrys = []
for _ in range(n):
    jewelrys.append(tuple(map(int, input().strip().split()))) # 무게, 가격
bags = []
for _ in range(k):
    bags.append(int(input().strip()))

jewelrys.sort(key = lambda x: -x[1])
bags.sort()
ans = 0
for j_weight, j_value in jewelrys:
    for i, bag in enumerate(bags):
        if bag >= j_weight:
            ans += j_value
            bags[i] = -1
            break
print(ans)
