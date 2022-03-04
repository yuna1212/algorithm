"""
시작 시간: 2022년 3월 4일 오전 10시 10분
소요 시간: 10분
풀이 방법:
    1. 더이상 확률이 증가할 수 없는 경우를 미리 지움
    2. 게임 진행시, 확률이 지금보다 작아지는 경우는 없음(같거나, 크거나)
       이를 기준으로 경우를 나눠 구간을 분할함
    3. 반복 종료 조건은 구간 길이가 1보다 작아지는 경우
    4. 반복문 진입 전, mid 또는 점수 계산에 대한 과정은 필요하지 않음
"""
global L
L = 2000000000

def ratio(b, a):
    return (a*100) / b

def neededGames(games, won):
    global L
    
    # 불가능한 경우 미리 거르기
    if ratio(games, won) == ratio(games + L, won + L):
        return -1
    
    lo, hi = 0, L
    while lo+1 < hi:
        mid = (lo + hi) // 2
        if ratio(games, won) == ratio(games + mid, won + mid):
            # 이전 확률과 동일하게 나온다면, 왼쪽 구간을 지움
            lo = mid
        else:
            # 이전 확률보다 크게 나온다면, 오른쪽 구간을 지움
            hi = mid
    return hi