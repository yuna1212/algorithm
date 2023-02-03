"""
시작 시간: 2023-02-03 10:46 AM
소요 시간: 20분
풀이 방법:
    - heap으로 풀 이유 없음
    - 저장되는 값들은 내림차순이기 때문에 stack으로, 가장 마지막값부터 확인하면 ok
"""
import heapq
def solution(numbers):
    answer = [-1] * len(numbers)
    mins = [(numbers[0], 0)]

    for i in range(1, len(numbers)):
        number = numbers[i]

        while mins:
            min_value, min_index = mins[0]

            if min_value >= number:
                break

            answer[min_index] = number
            heapq.heappop(mins)

        heapq.heappush(mins, (number, i))

    return answer

print(solution([2, 3, 3, 5]))
