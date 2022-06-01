"""
시작 시간: 2022년 6월 1일 오후 10시 50분
소요 시간: 
풀이 방법:
    다른 사람 풀이 보고 해결,, https://velog.io/@eehwan/프로그래머스-풍선-터트리기-파이썬
    '양 옆에서 구한 최솟값중 하나라도 크면 된다'라는 아이디어는 동일했지만 O(N)으로 해결할 수 있었다.
    
    '최솟값'을 어떻게 기억할 수 있을지 고민했다면 좋았을듯..
"""

INF = 1000000000
def solution(a):
    result = [False for _ in range(len(a))]
    minFront, minRear = INF, INF
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            result[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            result[-1-i] = True
    return sum(result)
solution([9,-1,-5])
