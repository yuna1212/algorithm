"""
시작 시간: 2022-09-08 PM 05:01
소요 시간: 50분
풀이 방법:
    - 재귀해도 depth가 100이므로 재귀로 품
"""
MIN = 10**10
MAX = -10**10
def div(first, second):
    if first < 0:
        first = -first
        return -(first // second)
    return first // second

def calc(number_idx, result, operators_count):
    global NUMBERS, MIN, MAX, OPERATORS_COUNT
    if number_idx == len(NUMBERS):
        MIN = min(MIN, result)
        MAX = max(MAX, result)
        return
    if OPERATORS_COUNT[0] > operators_count[0]:
        calc(number_idx+1, result + NUMBERS[number_idx], (operators_count[0]+1, operators_count[1], operators_count[2], operators_count[3]))
    if OPERATORS_COUNT[1] > operators_count[1]:
        calc(number_idx+1, result - NUMBERS[number_idx], (operators_count[0], operators_count[1]+1, operators_count[2], operators_count[3]))
    if OPERATORS_COUNT[2] > operators_count[2]:
        calc(number_idx+1, result * NUMBERS[number_idx], (operators_count[0], operators_count[1], operators_count[2]+1, operators_count[3]))
    if NUMBERS[number_idx] != 0 and OPERATORS_COUNT[3] > operators_count[3]:
        calc(number_idx+1, div(result, NUMBERS[number_idx]), (operators_count[0], operators_count[1], operators_count[2], operators_count[3]+1))

NUMBERS = []
input()
NUMBERS = list(map(int, input().split()))
OPERATORS_COUNT = list(map(int, input().split()))
calc(1, NUMBERS[0], (0, 0, 0, 0))
print(MAX)
print(MIN)
