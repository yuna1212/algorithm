"""
시작 시간: 2022년 5월 20일 오후 3시 5분
소요 시간: 2분
풀이 방법:
"""

def solution(numbers):
    answer = set()
    size = len(numbers)
    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            answer.add(numbers[i]+numbers[j])
    answer = sorted(list(answer))
    return answer