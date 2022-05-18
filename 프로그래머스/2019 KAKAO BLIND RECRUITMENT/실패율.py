"""
시작 시간: 2022년 5월 18일 오후 10시 10분
소요 시간: 30분
풀이 방법:
    복잡한 sort, key에 리턴을 2개 줘서 여러 조건으로 sorting
"""

def solution(N, stages):
    answer = []
    challenging_users_at = [0] * (N+2)
    for stage in stages:
        challenging_users_at[stage] += 1
    
    # 실패율 구하기
    failure_ratio = [] # (ratio, stage)
    arrived_users = challenging_users_at[-1]
    for stage in range(N, 0, -1):
        ratio = 0
        arrived_users += challenging_users_at[stage]
        if arrived_users != 0:
            ratio = challenging_users_at[stage]/arrived_users
        failure_ratio.append((ratio, stage))
    
    failure_ratio.sort(key=lambda x:(-x[0], x[1]))
    for _, stage in failure_ratio:
        answer.append(stage)
    return answer

solution(4, [4,4,4,4,4])