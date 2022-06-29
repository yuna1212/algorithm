"""
시작 시간: 2022년 6월 29일 오후 2시 40분
소요 시간: 50분
풀이 방법: 
    이분탐색 했는데 효율성에서 부분통과ㅠㅠ
"""
def get_ranges(gems, length, range_start):
    for i in range(len(gems) - length + 1):
        kind_having = set(gems[range_start+i:range_start+i+length])
        if kind_having == MUST_INCLUDE: 
            return range_start+i, range_start+i+length
    return None

def solution(gems):
    global MUST_INCLUDE
    MUST_INCLUDE = set(gems)
    
    min_length = len(MUST_INCLUDE) # 최소 보석 길이
    max_length = len(gems) # 최대 보석 길이
    range_start = 0
    range_end = len(gems)
    range_got = get_ranges(gems, len(MUST_INCLUDE), range_start)
    
    if range_got is not None: return range_got[0]+1, range_got[1]
    
    while max_length - min_length  > 1:
        middle = (max_length+min_length) // 2
        range_got = get_ranges(gems, middle, range_start)
        if range_got is not None: # 길이 더 짧아야
            range_start, range_end = range_got
            max_length = middle
        else: # 길이가 더 길어야
            min_length = middle
            
    return range_start+1, range_end