"""
시작 시간: 2023-02-19 01:00 PM
소요 시간: 1시간 50분
풀이 방법: 분할정복
    - 1이 몇 개 나오는지를 계산
    - 0이 몇 번 나오는지 계산할수도 있음
"""
def my_solution(n, l, r):
    # n번째 칸토어[l:r]의 1의 개수를 구함
    length = 5**n
    k = length // 5

    if k == 1:
        return '11011'[l:r].count('1')

    answer = 0
    nl, nr= l, -1
    while True:
        if nl > r: 
            break
            
        index = nl // k
        nr = (index + 1)*k

        if index == 2:
            nl = nr
            continue

        base = nr - k
        
        if nr >= r:
            answer += my_solution(n-1, nl - base, r - base)
            break

        answer += my_solution(n-1, nl - base, nr - base)
        nl = nr

    return answer

def solution(n, l, r):
    return my_solution(n, l - 1, r)
