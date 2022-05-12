"""
시작 시간: 2022년 5월 12일 오전 10시 55분
소요 시간: 35분
풀이 방법:
    시간초과!
    각각의 문자열이 가지고있는 알파벳으로, 알파벳을 키로하여 그 알파벳이 있는 위치를 값에 저장하는 딕셔너리를 만듦
    둘중 하나의 딕셔너리에서 모든 원소를 순차로 탐색해서,
    그 원소로 시작하는 다른 문자열 위치와 비교하면서 공통 길이 구하기
    
    시간복잡도는 O(N+M+N*M)...?
"""
def solution(s1, s2):
    s1_alpha_position = get_alphabet_positions(s1) # -> M
    s2_alpha_position = get_alphabet_positions(s2) # -> N
    s2_keys = set(s2)
    loggest_common_length = 0
    for alpha, s1_start_positions in s1_alpha_position.items(): # -> 최대 26
        if alpha not in s2_keys: continue # 공통 문자가 아니면 넘어가기
        
        s2_start_positions = s2_alpha_position[alpha] # 공통 문자로 시작하는 s2의 인덱스 구하기
        
        for s1_start_position in s1_start_positions: # -> 
            for s2_start_position in s2_start_positions:
                loggest_common_length = find_common_substring_length(s1, s1_start_position, s2, s2_start_position, loggest_common_length)
    return loggest_common_length
            
def get_alphabet_positions(string) -> dict:
    dict = {}
    for alpha in set(string):
        dict[alpha] = []
    for i, c in enumerate(string):
        dict[c].append(i)
    return dict

def find_common_substring_length(s1, s1_start_index, s2, s2_start_index, loggest_common_length):
    common_substring_length = loggest_common_length
    i = 0
    while i < loggest_common_length and s1_start_index+i < len(s1) and s2_start_index+i < len(s2):
        if s1[s1_start_index+i] == s2[s2_start_index+i]:
            i += 1
        else:
            break
    if i == loggest_common_length:
        while s1_start_index+i < len(s1) and s2_start_index+i < len(s2):
            if s1[s1_start_index+i] == s2[s2_start_index+i]:
                common_substring_length += 1    
                i += 1
            else:
                break
    return common_substring_length

print(solution(input(), input()))