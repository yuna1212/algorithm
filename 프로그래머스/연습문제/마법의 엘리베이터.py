"""
시작 시간: 2023-01-21 12:15 AM
소요 시간: 40분
풀이 방법:
"""
INF = 10**9

def get_min_magic_stone(floor, cost, exponent):
    if floor == 0: return cost
    if floor >= INF: return INF
    unit = 10**exponent
    rest = floor % (unit*10)

    down_cost = rest // unit
    down_floor = floor - rest
    up_cost = 10 - down_cost
    up_floor = down_floor + unit*10

    exponent += 1
    return min(get_min_magic_stone(down_floor, cost+down_cost, exponent), \
            get_min_magic_stone(up_floor, cost+up_cost, exponent))

def solution(storey):
    answer = 0
    return get_min_magic_stone(storey, 0, 0) 

