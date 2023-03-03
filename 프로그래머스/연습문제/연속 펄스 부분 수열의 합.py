"""
시작 시간: 2023-03-03 11:39 PM
소요 시간: 30분
풀이 방법: 그리디
"""
def get_max(sequence, pulse):
    sum_up = 0
    ret = -1
    for now in sequence:
        if sum_up < 0:
            sum_up = now * pulse
        else:
            sum_up += now * pulse

        ret = max(ret, sum_up)
        pulse *= -1

    return ret

def solution(sequence):
    return max(get_max(sequence, 1), get_max(sequence, -1))
