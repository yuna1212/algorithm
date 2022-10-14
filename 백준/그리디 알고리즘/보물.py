"""
시작 시간: 2022-10-14 02:30 AM
소요 시간: 10분
풀이 방법: 정렬.. 너무 단순한 그리디
"""
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(n):
    ans += a[i]*b[i]
print(ans)
