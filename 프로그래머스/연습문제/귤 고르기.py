"""
시작 시간: 2023-02-21 09:13 PM
소요 시간: 20분
풀이 방법: 맵과 정렬
"""
from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    tangerin_types = defaultdict(int)

    for t in tangerine:
        tangerin_types[t] += 1

    tangerine = [ tangerin_types[k] for k in sorted(tangerin_types.keys(), key = lambda k: -tangerin_types[k]) ]

    for i in range(len(tangerine)):
        k -= tangerine[i]
        answer += 1
        if k <= 0:
            break

    return answer
