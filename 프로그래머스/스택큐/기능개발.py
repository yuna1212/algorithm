"""
시작 시간: 2022년 2월 15일 오전 12시 55분
소요 시간: 40분
풀이 방법:
    일정 구간에서, max보다 작은 것은 한번에 배포할 수 있다는 특징 사용.
    큐로 구현: 리스트의 앞쪽에 있는것이 먼저 달성이 되어있어야하므로.
"""
from math import ceil
def solution(progresses, speeds):
    answer = []
    left = list(map(lambda i: ceil((100-progresses[i])/speeds[i]), range(len(progresses))))
    
    max = left.pop(0)
    pubCount = 1
    while left:
        new = left.pop(0)
        if new <= max:
            pubCount += 1
        else:
            max = new
            answer.append(pubCount)
            pubCount = 1
    answer.append(pubCount)
    return answer

print(solution(	[93, 30, 55], [1, 30, 5]))