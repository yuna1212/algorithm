"""
시작 시간: 2022년 6월 29일 오후 2시
소요 시간: 20분
풀이 방법: 
    우선순위 따라서 연산 차례로 해줬다. O(3N) = O(N)
    나는 배열에다가 직접 연산 해줬는데, 다른사람 풀이 보니까 문자열을 eval로 평가한 결과값 반복적으로 써서 코드 깔끔하게 품
"""
import re
from itertools import permutations
def get_numbers_and_operands(expression):
    operands = re.findall(r"[\+\-\*]", expression)
    numbers = re.findall(r"\d+", expression)
    return list(map(int, numbers)), operands

def get_permutations_of_operands(operands):
    operands = set(operands)
    return permutations(operands, len(operands))

def calc(numbers, operands, priority):
    numbers = numbers[:]
    for op in priority:
        for i in range(len(operands)):
            if operands[i] != op: # 연산해야할 연산자 아니면 넘어가기
                continue
            j = i+1
            while numbers[j] is None:
                j += 1
            if op == "+": numbers[j] += numbers[i]
            elif op == "-": numbers[j] = numbers[i] - numbers[j]
            elif op == "*": numbers[j] *= numbers[i]
            numbers[i] = None
    return numbers[-1]
            
def solution(expression):
    answer = 0
    numbers, operands = get_numbers_and_operands(expression)
    operand_priorities = get_permutations_of_operands(operands)
    for priority in operand_priorities:
        answer = max(answer, abs(calc(numbers, operands, priority)))
    return answer