"""
시작 시간: 2022년 6월 23일 오후 11시 35분
소요 시간: 1시간 10분
풀이 방법: 연산자 기준으로 조합 써서 했는데, 생각해보니까 연속된 연산자는 각각에다가 괄호를 씌울 수 없다..

- combinations 함수 직접 작성: 연속된 연산자는 괄호 사용 불가
- deepcopy 대신 slicing 사용: 원시타입의 1차원 리스트만 사용하므로
"""
def operate(preceding_number, following_number, operator):
    if operator == "*": return preceding_number * following_number
    if operator == "+": return preceding_number + following_number
    if operator == "-": return preceding_number - following_number
    return preceding_number
def calculate(numbers, operators):
    for i in range(len(operators)):
        numbers[i+1] = operate(numbers[i], numbers[i+1], operators[i])
    return numbers[-1]
def combinations(n, r):
    ret = []
    stack = [[i] for i in range(n)]
    while stack:
        elements = stack.pop()
        if len(elements) == r:
            ret.append(elements)
            continue
        for i in range(elements[-1]+2, n):
            next_elements = elements[:]
            next_elements.append(i)
            stack.append(next_elements)
    return ret

n = int(input())
line = input()
numbers = []
operators = []
for i in range(0, n, 2):
    numbers.append(int(line[i]))
for i in range(1, n, 2):
    operators.append(line[i])

# 괄호가 하나도 없을 때
result = numbers[:]
ret = calculate(result, operators)
for r in range(len(operators)):
    combs = combinations(len(operators), r)
    for comb in combs:
        result = numbers[:]
        copied_operators = operators[:]
        for i in comb:
            calc_ret = calculate(result[i:i+2], copied_operators[i:i+1])
            result[i] = calc_ret
            result[i+1] = calc_ret
            copied_operators[i] = None
        calculate(result, copied_operators)
        ret = max(ret, result[-1])
print(ret)