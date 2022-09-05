"""
시작 시간: 2022-09-05 AM 09:36
소요 시간: 1시간 30분 
풀이 방법:
    - 각 상담의 마지막날 돈을 받는 것을 가정
    - 각 날짜에서, 전날의 금액, 오늘 끝나는 상담을 포함할 때 얻는 전체 이익 중 큰 것을 dp 테이블에 저장
    - 같은 날에 여러 상담이 같이 끝날 수 있으므로, 끝나는 날 을 인덱스로 리스트에 시작일, 기간, 이익을 리스트에 저장
"""
def input_file(path):
    global N, POSSIBLE_RESERVATIONS
    f = open(path)
    N = int(f.readline().strip())
    POSSIBLE_RESERVATIONS = [[] for _ in range(N)] 
    for start_day in range(N):
        period, benefit = tuple(map(int, f.readline().strip().split())) 
        end_day = start_day + period - 1
        if end_day < N:
            POSSIBLE_RESERVATIONS[start_day+period-1].append((start_day, period, benefit))
def input_data():
    global N, POSSIBLE_RESERVATIONS
    N = int(input())
    POSSIBLE_RESERVATIONS = [[] for _ in range(N)] 
    for start_day in range(N):
        period, benefit = tuple(map(int, input().split())) 
        end_day = start_day + period - 1
        if end_day < N:
            POSSIBLE_RESERVATIONS[start_day+period-1].append((start_day, period, benefit))

global N, POSSIBLE_RESERVATIONS
input_data()
dp = [0] * N
for day in range(N):
    reservations = POSSIBLE_RESERVATIONS[day]
    for reservation in reservations:
        if not reservation:
            continue
        start_day, period, benefit = reservation
        dp[day] = max(dp[day], dp[max(day-1, 0)], dp[max(0, start_day-1)] + benefit)
    if not reservations:
        dp[day] = dp[day-1]
print(dp[N-1])
