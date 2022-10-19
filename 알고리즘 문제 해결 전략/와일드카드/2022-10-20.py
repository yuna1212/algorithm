"""
시작 시간: 2022-10-20 02:17 AM
소요 시간: 1시간 30분
풀이 방법:
"""
def is_ok(standard, compare):
    # cache 초기화
    cache = [[False]*len(compare) for _ in range(len(standard))]
    if standard[0] == '*':
        for i in range(len(compare)):
            cache[0][i] = True
    elif standard[0] == '?':
        cache[0][0] = True
    elif standard[0] == compare[0]:
        cache[0][0] = True
    for i in range(len(standard)):
        if standard[i] != '*': break
        cache[i][0] = True

    # dp 채우기
    for i in range(1, len(standard)):
        for j in range(1, len(compare)):
            cache[i][j] = cache[i-1][j-1] and ((standard[i] == compare[j]) or (standard[i] == '*') or standard[i] == '?')

    if compare == 'help':
        print(cache)
    return cache[len(standard)-1][len(compare)-1]


def solution():
    compares = []
    standard = input()
    n = int(input())
    for _ in range(n):
        compare = input()
        if is_ok(standard, compare):
            print('>>', compare)
        
for _ in range(int(input())):
    solution()
   
