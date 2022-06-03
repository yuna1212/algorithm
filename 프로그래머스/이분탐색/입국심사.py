"""
시작 시간: 2022년 6월 3일 오후 2시 5분
소요 시간: 1시간 30분
풀이 방법:
    전체 입국심사에 걸리는 시간을 기준으로 이분탐색
    특정 시간 t에 처리할 수 있는 사람 수가 n보다 커도, t가 답이 될 수 있음에 유의
    n이 10^9, times 길이는 10^5이기 때문에 이분탐색
"""
def get_immigration_count(whole_time, times):
    if whole_time <= 0:
        return 0
    immigration_count = 0
    for time in times:
        immigration_count += whole_time // time
    return immigration_count
    
def solution(n, times):
    answer = 0
    times.sort()
    
    right = times[0] * n
    left = 0
    
    if get_immigration_count(right, times) == n:
        answer = right
    while right - left > 1:
        middle = (right+left) // 2
        immigration_count = get_immigration_count(middle, times)
        
        if immigration_count < n:
            left = middle
        else:
            right = middle
            answer = middle
    return answer