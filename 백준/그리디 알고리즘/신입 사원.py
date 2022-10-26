"""
시작 시간: 2022-10-27 02:08 AM
소요 시간: 10분
풀이 방법:
"""
import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    scores = [] # ( 서류 성적, 면접 성적), min heap
    # 입력
    for _ in range(int(input().strip())):
        apply_scores = tuple(map(int, input().strip().split()))
        heapq.heappush(scores, apply_scores)

    # 비교
    _, min_score = heapq.heappop(scores)
    ans = 1
    while scores:
        _, apply_score = heapq.heappop(scores)
        if apply_score < min_score:
            min_score = apply_score
            ans += 1
    print(ans)
