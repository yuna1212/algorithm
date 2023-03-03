"""
시작 시간: 2023-03-03 11:23 PM
소요 시간: 10분
풀이 방법: 단순한 그리디
"""
def solution(n, m, section):
    result = 0
    now = 0
    for s in section:
        if s < now:
            continue

        if s > now:
            now = s

        if s == now:
            result += 1
            now += m

    return result
