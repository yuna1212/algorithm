"""
시작 시간: 2022-11-22 09:15 PM
소요 시간: 2시간 30분
풀이 방법: 정렬 후 두 가지 조건(앞서 사용한 깊콘보다 후에 사용, 기한이 계획 이상)에 맞춰 앞에서부터 탐색, 초기값 설정에 몹시 주의하기
"""
import math
n = int(input())
deadlines = list(map(int, input().split()))
plans = list(map(int, input().split()))
sorted_indecies = sorted([i for i in range(n)], key= lambda x: plans[x]) # plan에 따라 정렬

ans = 0
index = sorted_indecies[0]
if plans[index] > deadlines[index]:
    expanding_counter = math.ceil((plans[index] - deadlines[index])/30)
    deadlines[index] += 30*expanding_counter
    ans += expanding_counter

max_deadline = deadlines[index] 
time = 0 
last_plan = plans[index]
for i in range(1, n):
    index = sorted_indecies[i]
    
    if last_plan != plans[index]:
        time = max_deadline

    if plans[index] > deadlines[index]:
        # 계획에 맞춰 연장
        expanding_counter = math.ceil((plans[index] - deadlines[index])/30)
        deadlines[index] += 30*expanding_counter
        ans += expanding_counter

    if deadlines[index] < time:
        # 이전 것 보다 뒤에 쓰도록 연장
        expanding_counter = math.ceil((time - deadlines[index]) / 30)
        deadlines[index] += 30*expanding_counter
        ans += expanding_counter

    if last_plan == plans[index]:
        max_deadline = max(max_deadline, deadlines[index])
    else:
        max_deadline = deadlines[index]
        last_plan = plans[index]
        
print(ans)
