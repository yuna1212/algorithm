"""
시작 시간: 2023-02-17 03:18 PM
소요 시간: 1시간 30분
풀이 방법: 변수가 2개면 하나를 고정시키고 탐색
    - 업무 점수를 내림차순 정렬 후, 동료 점수 조건에 맞지 않는 것을 제하기
"""
def solution(scores):
    answer = 1
    target_sum = scores[0][0] + scores[0][1]
    target_work = scores[0][0]
    target_peer = scores[0][1]
    
    scores.sort(key = lambda x: (-x[0], x[1])) # 업무평가 내림차순, 동일시 동료평가 오름차순

    prev_peer = -1
    prev_work = -1
    for work_score, peer_score in scores:
        if target_work < work_score and target_peer < peer_score: 
            return -1

        if peer_score < prev_peer and work_score < prev_work:
            # 인센티브 받는 바로 이전 것에 못미치는 경우 pass
            continue

        if target_sum < work_score + peer_score:
            answer += 1

        prev_peer = peer_score
        prev_work = work_score

    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))
