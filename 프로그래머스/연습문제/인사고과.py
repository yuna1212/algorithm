"""
시작 시간: 2023-02-17 12:45 PM
소요 시간: 1시간 50분
풀이 방법: 두개 기준따라 정렬 후, 끝에서부터 비교
    - [ (7, 20), (9, 11), (8, 10), (10, 20) ]에서 세번째 사원 인센티브 못거름
"""
import heapq
WORK = 0
PEER = 1
ID = 2
def solution(scores):
    for i in range(len(scores)):
        scores[i].append(i)

    scores_by_work = sorted(scores, key = lambda x: x[0])
    scores_by_peer = sorted(scores, key = lambda x: x[1])
    multi_scores = []

    work_i = len(scores) - 1
    best_worker = scores_by_work[work_i]
    for worst_peer in scores_by_peer: 

        if best_worker[WORK] > worst_peer[WORK] and best_worker[PEER] > worst_peer[PEER]:
            # 가장 높은 업무 점수 사원과 가장 낮은 동료 점수 사원을 비교
            # 가장 낮은 동료 점수 사원이 모두 부족하다면 인센티브 제외
            continue

        heapq.heappush(multi_scores, (-(worst_peer[WORK] + worst_peer[PEER]), worst_peer[ID]))

        if best_worker[ID] == worst_peer[ID]: 
            work_i -= 1
            best_worker = scores_by_work[work_i]

    rank = 0
    prev_score = 1 # 없는 값으로 초기화
    people = 1
    while multi_scores:
        score, id = heapq.heappop(multi_scores)

        if prev_score != score:
            prev_score = score
            rank += people
            people = 1
        else:
            people += 1

        if id == 0:
            return rank

    return -1

