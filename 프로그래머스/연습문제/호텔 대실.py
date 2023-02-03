"""
시작 시간: 2023-02-03 03:30 PM
소요 시간: 30분
풀이 방법: O(NlogN)이 아니라 O(N)으로 풀 수 있음
"""
import heapq

def convert(time):
    hour, minute = time.split(":")
    return int(hour)*60+int(minute)

def solution(book_time):
    answer = 0
    book_time = sorted(list(map(lambda time: [convert(time[0]), convert(time[1])], book_time)))
    ready_times = []

    for checkin_time, checkout_time in book_time:
        if ready_times and ready_times[0] <= checkin_time:
            heapq.heappop(ready_times)
        else:
            answer = max(answer, len(ready_times) + 1)

        heapq.heappush(ready_times, checkout_time + 10)

    return answer
