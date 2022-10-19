"""
시작 시간: 2022-10-19 03:37 PM
소요 시간: 10분
풀이 방법: set로 간단하게 집합 표현
"""
n, m = map(int, input().split())
never_heards= set()
for _ in range(n):
    never_heards.add(input())
answer = set()
for _ in range(m):
    never_seen = input()
    if never_seen in never_heards:
        answer.add(never_seen)
print(len(answer))
answer = sorted(list(answer))
for p in answer:
    print(p)
