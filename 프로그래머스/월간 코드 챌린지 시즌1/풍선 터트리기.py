"""
시작 시간: 2022년 6월 1일 오전 12시
소요 시간: 50분
풀이 방법:
    brute force
"""

# 시간초과: O(N^2)인데 N이 최대 1,000,000인 것이 문제일듯
def solution(a):
    answer = 2
    for i in range(1, len(a) - 1):
        remaining = a[i]
        left_min = min(a[:i])
        right_min = min(a[i+1:])
        if left_min < remaining and right_min < remaining:
            answer -= 1
        answer += 1
    return answer