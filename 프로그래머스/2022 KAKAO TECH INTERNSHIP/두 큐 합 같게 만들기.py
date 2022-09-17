"""
시작 시간: 2022-09-17 08:09 PM
소요 시간: 2시간 10분
풀이 방법:
    - 순서대로 덧셈
    - 시간초과와 오답
"""
def count(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target_sum = (sum1+sum2)//2

    if sum1 == target_sum: return 0

    for i in range(len(queue1)):
        sum1 -= queue1[i] 
        summing = sum1
        if sum1 == target_sum: return i+1
        for j in range(len(queue2)):
            summing += queue2[i] 
            if summing == target_sum: return i + j + 2
            if summing > target_sum: break
    
    counter = None
    for i in range(len(queue1)):
        summing = 0
        for j in range(i, len(queue1)):
            summing += queue1[j]
            if summing == target_sum:
                if counter: counter = min(counter, j+j+1+len(queue2))
                else: counter = i+j+1+len(queue2)
                break
            if summing > target_sum: break

    if counter is None: return -1 
    return counter

def solution(queue1, queue2):
    sum_up = sum(queue1)+sum(queue2) 
    if sum_up % 2 == 1: 
        return -1

    result1 = count(queue1, queue2)
    if result1 == -1: return count(queue2, queue1)
    result2 = count(queue2, queue1)
    if result2 == -1: return result1
    return min(result1, result2)

