"""
시작 시간: 2023-03-11 06:01 PM
소요 시간: 10분
풀이 방법:
"""
n, m = map(int, input().split())
name_of = [None]*(n+1)
index_of = dict()
for i in range(n):
    name = input()
    name_of[i+1] = name
    index_of[name] = i+1 

for _ in range(m):
    question = input()
    if question.isdigit():
        print(name_of[int(question)])
    else:
        print(index_of[question])


