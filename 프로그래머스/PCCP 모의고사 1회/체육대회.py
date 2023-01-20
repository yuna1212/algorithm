"""
시작 시간: 2023-01-20 05:53 PM
소요 시간: 30분
풀이 방법:
"""
def solution(ability):
    answer = 0
    global ABILITY
    ABILITY = ability
    answer = get_best_score(set(i for i in range(len(ability))), 0, 0)

    return answer

def get_best_score(rest_students, subject, score):
    global ABILITY
    if subject == len(ABILITY[0]): return score

    best_score = score

    for student in rest_students:
        best_score = max(best_score, get_best_score(rest_students - set([student]), subject + 1, score + ABILITY[student][subject]))
    
    return best_score

