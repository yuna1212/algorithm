"""
시작 시간: 2022년 3월 20일 오전 2시 40분
소요 시간: 1시간
풀이 방법:
    중앙값을 기준으로, 중앙값보다 작은 입력들은 최대힙에 큰 입력들은 최소힙에 넣음
    입력이 들어올때마다 최소 또는 최대힙에서 값 꺼내서 중앙값으로 바꿔주거나 원래 중앙값 유지
"""
from sys import stdin
import heapq
n = int(stdin.readline())
median = int(stdin.readline())
print(median)
max_heap = []
min_heap = []
number_counter = 1
for _ in range(n-1):
    new_number = int(stdin.readline())
    if number_counter % 2:
        # 홀수개일 때 새로운 입력이 들어온 경우
        if new_number < median:
            heapq.heappush(max_heap, -new_number)
            heapq.heappush(min_heap, median)
            median = -heapq.heappop(max_heap)
        else:
            heapq.heappush(min_heap, new_number)
    else:
        # 짝수개일때 새로운 입력
        if new_number < median:
            heapq.heappush(max_heap, -new_number)
        else:
            heapq.heappush(min_heap, new_number)
            heapq.heappush(max_heap, -median)
            median = heapq.heappop(min_heap)
    number_counter += 1
    print(median)