"""
시작 시간: 2023-01-05 02:49 PM
소요 시간: 40분
풀이 방법: 그리디! 파이썬의 힙 모듈은 min heap인 것 유의
"""
import heapq

def solution(n, k, enemy):
    enemies_dead = []
    ans = 0
    for round, e in enumerate(enemy):
        heapq.heappush(enemies_dead, -e)
        n -= e
        while n < 0:
            if k == 0:
                return round

            n -= heapq.heappop(enemies_dead)
            k -= 1

    return len(enemy)
