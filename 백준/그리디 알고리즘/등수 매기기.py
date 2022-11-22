"""
시작 시간: 2022-11-22 08:41 PM
소요 시간: 10분
풀이 방법: 앞에서부터 차곡차곡 체크하며 답 구하기
"""
import sys
input = sys.stdin.readline
n = int(input().strip())
scores = []
for _ in range(n):
    scores.append(int(input().strip()))
scores.sort()
ans = 0
for i in range(n):
    ans += abs(i+1 - scores[i])
print(ans)
