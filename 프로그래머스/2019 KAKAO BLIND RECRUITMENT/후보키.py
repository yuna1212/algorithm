"""
시작 시간: 2022년 5월 18일 오후 11시
소요 시간: 1시간 40분
풀이 방법:
    combination 모듈 사용해서 모든 경우의수에서 조건 확인
"""
# CANDIDATE_KEY_COUNTER = 0
# def is_candidate_key(attributes, relation):
#     value_set = set()
#     for a_tuple in relation:
#         a_value = tuple(a_tuple[attribute] for attribute in attributes)
#         if a_value in value_set:
#             return False
#         value_set.add(a_value)
#     return True

# def update_candidate_key_counter(base_attributes: list, additive_attributes: list, relation: list):
#     # 단, base_attributes는 후보키가 아닌 키들이다.
#     global CANDIDATE_KEY_COUNTER
#     for i, additive_attribute in enumerate(additive_attributes):
#         next_base_attribute = base_attributes + [additive_attribute]
#         if not is_candidate_key(next_base_attribute, relation):
#             update_candidate_key_counter(next_base_attribute, additive_attributes[i+1:], relation)
#         else:
#             CANDIDATE_KEY_COUNTER += 1

# def solution(relation):
#     global CANDIDATE_KEY_COUNTER
#     attribute_size = len(relation[0])
#     base_attributes = []
#     for i in range(attribute_size):
#         if not is_candidate_key([i], relation):
#             base_attributes.append(i)
#         else:
#             CANDIDATE_KEY_COUNTER += 1
#     for i in range(len(base_attributes)):
#         update_candidate_key_counter([base_attributes[i]], base_attributes[i+1:], relation)
    
    
#     return CANDIDATE_KEY_COUNTER

# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

from itertools import combinations
CANDIDATE_KEYS = []
def is_candidatable(attributes, relation):
    global CANDIDATE_KEYS
    # 최소성 만족
    for candidate_key in CANDIDATE_KEYS:
        if candidate_key.issubset(attributes):
            return False
    # 유일성 만족
    value_set = set()
    for a_tuple in relation:
        a_value = tuple(a_tuple[attribute] for attribute in attributes)
        if a_value not in value_set:
            value_set.add(a_value)
        else:
            return False
    return True

def solution(relation):
    attribute_size = len(relation[0])
    attributes = [i for i in range(attribute_size)]
    for candidates_length in range(1, attribute_size+1):
        for comb in combinations(attributes, candidates_length):
            if is_candidatable(comb, relation):
                CANDIDATE_KEYS.append(set(comb))
    return len(CANDIDATE_KEYS)