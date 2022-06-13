"""
시작 시간: 2022년 6월 13일 오전 11시 35분
소요 시간: 5분
풀이 방법: -
"""
def solution(absolutes, signs):
    answer = 0
    size = len(absolutes)
    for i in range(size):
        absolute, sign = absolutes[i], signs[i]
        answer += absolute * (1 if sign else -1)
    return answer