"""
시작 시간: 2023-02-21 06:33 PM
소요 시간: 10분
풀이 방법: 단순한 수학 문제 풀이
"""
def solution(k, d):
    answer = 0
    for a in range(d//k+1):
        answer += int(((d/k)**2 - a**2)**0.5) + 1
    return answer
