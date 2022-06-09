"""
시작 시간: 2022년 6월 9일 오전 10시 45분
소요 시간: 40분
풀이 방법:
    효율적으로 탐색하기 위해 두 리스트 정렬.
    이후 리스트를 각각 한번씩만 순회한다.
"""
def count_ensured_and_zeros(lottos, win_nums):
    lottos.sort(); win_nums.sort();
    i, j = 0, 0
    counter = 0
    
    while i < len(lottos) and lottos[i] == 0:
        i += 1
        
    zeros = i
    
    while i < len(lottos):
        while j < len(win_nums) and lottos[i] > win_nums[j]:
            j += 1
        if j >= len(win_nums):
            break
        if lottos[i] == win_nums[j]:
            counter += 1
            j += 1
        i += 1
    return counter, zeros

def get_rank(counting_matched):
    rank = 6 - counting_matched + 1
    if rank > 6:
        rank = 6
    return rank
    
    
def solution(lottos, win_nums):
    counting_ensured, zeros = count_ensured_and_zeros(lottos, win_nums)
    return get_rank(counting_ensured+zeros), get_rank(counting_ensured)

print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))