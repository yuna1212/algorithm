"""
시작 시간: 2023-02-04 12:22 AM
소요 시간: 10분
풀이 방법:
"""
def convert(time):
    hour, minute = time.split(":")
    return int(hour)*60+int(minute)

def solution(book_time):
    answer = 0
    time_table = [0] * (24 * 60 + 10)

    for time in book_time:
        checkin_time, checkout_time = [ convert(t) for t in time ]
        time_table[checkin_time] += 1
        time_table[checkout_time+10] -= 1

    accum = 0
    for using_state in time_table:
        accum += using_state
        answer = max(answer, accum)

    return answer
