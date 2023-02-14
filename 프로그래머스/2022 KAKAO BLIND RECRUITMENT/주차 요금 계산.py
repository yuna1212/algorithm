"""
시작 시간: 2023-02-14 02:01 PM
소요 시간: 50분
풀이 방법: 출차되지 않은 차량을 관리하기 위해, 차량의 입출차 상태를 관리하는 status 변수를 사용할 수도 있겠다.
"""
def update(accumulated_time, car, time):
    if car in accumulated_time:
        accumulated_time[car] += time
    else:
        accumulated_time[car] = time

def get_stay_time(entrance_time, leave_time):
    times = [] # entrance_time, leave_time을 분으로 환산
    for time in (entrance_time, leave_time):
        hours, minutes = map(int, time.split(':'))
        minutes += hours*60
        times.append(minutes)
        
    return times[1] - times[0]

def get_cost(stay_time, unit, cost_per_unit):
    unit_time = stay_time // unit
    if stay_time % unit != 0:
        unit_time += 1
    
    return unit_time*cost_per_unit

def solution(fees, records):
    answer = []
    accumulated_time = dict() # accumulated_time[차량번호] = 주차 누적 시간
    entrance_time = dict() # entrance_time[차량번호] = 입장 시각

    for record in records:
        time, car, status = record.split()
        if status[0] == 'I':
            entrance_time[car] = time
        else:
            stay_time = get_stay_time(entrance_time[car], time)
            del entrance_time[car]
            update(accumulated_time, car, stay_time)


    for car, entrance_time in entrance_time.items():
        stay_time = get_stay_time(entrance_time, '23:59')
        update(accumulated_time, car, stay_time)
    
    for car in sorted(accumulated_time.keys()):
        stay_time = accumulated_time[car]
        cost = 0
        if accumulated_time[car] <= fees[0]:
            cost = fees[1]
        else:
            cost = fees[1] + get_cost(stay_time - fees[0], fees[2], fees[3])

        answer.append(cost)

    return answer
