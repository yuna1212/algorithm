"""
시작 시간: 2023-01-20 09:48 PM
소요 시간: 1시간 20분
풀이 방법: 모든 세대를 구하면 시간초과. 입력 경우만 bottom-up으로 구하기
"""
DOMINANT = 0
HYBRID = 1
RECESSIVE = 2

def decode(gene_type):
    if gene_type == DOMINANT:
        return 'RR'
    elif gene_type == HYBRID:
        return 'Rr'
    else:
        return 'rr'

def get_children(a_parent):
    if a_parent == DOMINANT:
        return [DOMINANT]*4
    elif a_parent == HYBRID:
        return [DOMINANT, HYBRID, HYBRID, RECESSIVE]
    else:
        return [RECESSIVE]*4

"""
def get_nth_generation(now_generation, now_generation_num, target_generation_num):
    for i in range(now_generation_num+1, target_generation_num+1):
        next_generation = []
        for parent in now_generation:
            next_generation.extend(get_children(parent))
        now_generation = next_generation

    return now_generation 
"""
def get_type(generation_number, child_order):
    if generation_number == 1: return HYBRID

    parent = get_type(generation_number-1, child_order//4)
    return get_children(parent)[child_order%4]
    

def solution(queries):
    answer = []

    generation = [HYBRID]
    generation_num = 1

    for n, k in queries:
        answer.append(decode(get_type(n, k-1)))

    return answer

print(solution([[3, 1], [2, 3], [3, 9]]))

