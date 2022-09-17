"""
시작 시간: 2022-09-17 11:21 PM
소요 시간: 2시간
풀이 방법:
    - 데이터가 너무 많아서 brute force 불가
    - 크면 dequeue하고, 작으면 enqueue하는 식으로
    - 이미 계산해 둔 sum 값을 활용한다.
"""
def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target_sum = sum1 + sum2
    if target_sum % 2 == 1: return -1
    target_sum //= 2

    len1, len2 = len(queue1), len(queue2)
    start, end = 0, 0 
    whole_len = len1+len2
    summing = 0 
    count = 0
    while start < whole_len and end < whole_len+1:
        if summing < target_sum:
            if end < len2:
                summing += queue2[end]
            else:
                summing += queue1[end - len2]
            end += 1
        elif summing > target_sum:
            if start < len1:
                summing -= queue1[start]
            else:
                summing -= queue2[start - len1]
            start += 1
        else:
            return count
        count += 1
    return -1 

