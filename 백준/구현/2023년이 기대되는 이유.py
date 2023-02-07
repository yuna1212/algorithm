"""
시작 시간: 2023-02-07 12:56 AM
소요 시간: 1시간 10분
풀이 방법: 
"""
import sys
input = sys.stdin.readline
def calculate(numbers, operator_positions):
    result = 0
    j = 0
    for i in operator_positions:
        num = '0'
        while j <= i:
            num += numbers[j]
            j += 1
        result += int(num)

    num = '0'
    while j < len(numbers):
        num += numbers[j]
        j += 1

    result += int(num)
    return result 

def sum_up(numbers, operator_positions, results):
    results.add(calculate(numbers, operator_positions))

    for i in range(operator_positions[-1]+1, len(numbers) - 1):
        operator_positions.append(i)
        sum_up(numbers, operator_positions, results)
        operator_positions.pop()

def sum_by_m(numbers, m):
    result = 0
    for n in numbers:
        result += n**m
    return result
    
def solution(n):
    results_set = set([int(n)])

    for i in range(len(n) - 1):
        sum_up(n, [i], results_set)
        
    results = sorted(list(results_set))
    numbers = list(map(int, n))


    if numbers.count(1) == sum(numbers):
        return'Hello, BOJ 2023!' 

    answer = 0
    m = 1
    i = 0
    while True:
        result = results[i]
        left_result = 0
        
        while left_result < result:
            left_result = sum_by_m(numbers, m)
            m += 1

        while left_result > result:
            i += 1
            if i == len(results): return answer 
            result = results[i]
        

        if left_result == result:
            answer += 1



for _ in range(int(input().rstrip())):
    print(solution(input().rstrip()))
