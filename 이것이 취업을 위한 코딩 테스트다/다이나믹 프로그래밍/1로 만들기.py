"""
시작 시간: 2022년 4월 1일 오후 3시 55분
소요 시간: 10분
풀이 방법:
    DP
"""
x = int(input())
table = [0, 0]
for i in range(2, x+1):
    candidates = []
    if i%5 == 0:
        candidates.append(table[i//5]+1)
    if i%3 == 0:
        candidates.append(table[i//3]+1)
    if i%2 == 0:
        candidates.append(table[i//2]+1)
    candidates.append(table[i-1]+1)
    table.append(min(candidates))
print(table[-1])