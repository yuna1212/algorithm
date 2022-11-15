"""
시작 시간: 2022-11-16 02:42 AM
소요 시간: 10분
풀이 방법: 계수 정렬
"""
n = int(input())
names_score_of = [ [] for _ in range(101) ]
for _ in range(n):
    name, score = input().split()
    names_score_of[int(score)].append(name)

for names in names_score_of:
    for name in names:
        print(name, end=" ")
