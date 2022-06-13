"""
시작 시간: 2022년 6월 13일 오후 12시 45분
소요 시간: 45분
풀이 방법: 비트마스킹 했는데 시간초과
"""
"""
# 비트 마스킹
def count_diff_bit(smaller, bigger):
    # 마스크 구하기
    tmp = bigger
    mask = 1
    while tmp > 0:
        tmp >>= 1
        mask <<= 1
    
    # 다른 비트 개수 구하기
    result = smaller & bigger
    result |= mask
    counter = 0
    while result != 1:
        if result % 2 == 0:
            counter += 1
        result >>= 1
    return counter

def f(x):
    answer = x + 1
    while True:
        if count_diff_bit(x, answer) < 3:
            break
        answer += 1
    return answer

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(number))
    return answer
"""
def f(x):
    result = x
    mask = 1
    while result & mask: # 켜져있는한 계속
        mask <<= 1
    result |= mask # 꺼진 비트 켜기
    if x%2: # 홀수이면
        result &= ~(mask >> 1) # 켠 비트보다 하나 작은 비트 끄기
    return result
        
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(f(number)) # 한 줄 가능: f(x) = ((x^(x+1)) >> 2)+x+1 이다..
    return answer
    
print(solution([2, 7]))