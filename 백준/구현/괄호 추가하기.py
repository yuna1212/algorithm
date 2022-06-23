"""
시작 시간: 2022년 6월 23일 오후 11시 35분
소요 시간: 1시간 10분
풀이 방법: 연산자 기준으로 조합 써서 했는데, 생각해보니까 연속된 연산자는 각각에다가 괄호를 씌울 수 없다..
"""
from copy import deepcopy
from itertools import combinations
def operate(preceding_number, following_number, operator):
    if operator == "*": return preceding_number * following_number
    if operator == "+": return preceding_number + following_number
    if operator == "-": return preceding_number - following_number
    return preceding_number
def calculate(numbers, operators):
    for i in range(len(operators)):
        numbers[i+1] = operate(numbers[i], numbers[i+1], operators[i])
    return numbers[-1]


n = int(input())
line = input()
numbers = []
operators = []
for i in range(0, n, 2):
    numbers.append(int(line[i]))
for i in range(1, n, 2):
    operators.append(line[i])

ret = -100
operators_idx = [i for i in range(len(operators))]
for r in range(len(operators)):
    combs = combinations(operators_idx, r)
    for comb in combs:
        result = deepcopy(numbers)
        copied_operators = deepcopy(operators)
        for i in comb:
            calc_ret = calculate(result[i:i+2], copied_operators[i:i+1])
            result[i] = calc_ret
            result[i+1] = calc_ret
            copied_operators[i] = None
        calculate(result, copied_operators)
        ret = max(ret, result[-1])
print(ret)