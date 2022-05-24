"""
시작 시간: 2022년 5월 20일 오후 2시 45분
소요 시간: 1분
풀이 방법:
"""
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer