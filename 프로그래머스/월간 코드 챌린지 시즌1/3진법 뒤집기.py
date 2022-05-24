"""
시작 시간: 2022년 5월 20일 오후 2시 50분
소요 시간: 10분
풀이 방법:
"""
def get_reversed_ternary(number):
    ret = []
    while number // 3:
        ret.append(number % 3)
        number //= 3
    ret.append(number)
    return ret
def get_decimal(arr):
    ret = 0
    for i in range(len(arr)):
        ret += (3**i)*arr[-i-1]
    return ret
def solution(n):
    ternary = get_reversed_ternary(n)
    return get_decimal(ternary)