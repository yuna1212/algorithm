"""
시작 시간: 2022-09-17 07:42 PM
소요 시간: 30분
풀이 방법:
"""
def solution(survey, choices):
    answer = ''
    first_metrics = ['R', 'C', 'J', 'A']
    second_metrics = ['T', 'F', 'M', 'N']
    scores = [0] * 4
    for i in range(len(survey)):
        metrics = survey[i]
        score = choices[i]
        for j in range(4):
            if metrics[0] == first_metrics[j]:
                score -= 4
            elif metrics[1] == first_metrics[j]:
                score = 4 - score
            else: continue
            scores[j] += score
            break
    for i in range(len(scores)):
        if scores[i] > 0:
            answer += second_metrics[i]
        else:
            answer += first_metrics[i]
    return answer
