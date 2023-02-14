"""
시작 시간: 2023-02-14 03:00 PM
소요 시간: 2시간
풀이 방법: 재귀, DFS. 재귀 후 값 원상태로 복원해주는지, 잘못된 값을 업데이트해두진 않는지 체크하는게 중요
"""
def update(rest_arrows, target_score, apeach_score, lion_score):
    global APEACH_SCORES, LION_SCORES, ANSWER, MAX_SCORE_DIFF
    if target_score == len(APEACH_SCORES) or rest_arrows == 0:
        # 남은 화살 더하기
        last_win_score = 0
        ans = LION_SCORES[:]
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] != 0:
                last_win_score = i

        for i in range(last_win_score - 1, 0, -1):
            if rest_arrows > APEACH_SCORES[i]:
                ans[i] = rest_arrows
                lion_score = last_win_score
                rest_arrows = 0
                break

        if rest_arrows != 0:
            ans[0] += rest_arrows
        
        score_diff = lion_score - apeach_score
        if sum(ans) < 0:
            exit()
        if MAX_SCORE_DIFF < score_diff:
            MAX_SCORE_DIFF = score_diff
            ANSWER = ans
        return
    
    needed_arrows = APEACH_SCORES[target_score] + 1
    next_target_score = target_score + 1

    if needed_arrows <= rest_arrows:
        # 라이언이 맞추는 경우
        LION_SCORES[target_score] = needed_arrows
        if APEACH_SCORES[target_score] == 0:
            update(rest_arrows - needed_arrows, next_target_score, apeach_score, lion_score + target_score)
        else:
            update(rest_arrows - needed_arrows, next_target_score, apeach_score - target_score, lion_score + target_score)

        LION_SCORES[target_score] = 0

    # 어피치가 라이언 이상으로 맞추는 경우
    update(rest_arrows, next_target_score, apeach_score, lion_score)

def solution(n, info):
    global APEACH_SCORES, LION_SCORES, ANSWER, MAX_SCORE_DIFF

    info.reverse()
    APEACH_SCORES = info
    LION_SCORES = [0]*len(info)
    MAX_SCORE_DIFF = 0
    ANSWER = [-1]

    apeach_score = 0
    for i, score in enumerate(info):
        if score > 0:
            apeach_score += i

    update(n, 0, apeach_score, 0)
    
    ANSWER.reverse()
    return ANSWER 
