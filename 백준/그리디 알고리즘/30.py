"""
시작 시간: 2022-10-19 02:55 AM
소요 시간: 10분
풀이 방법:
"""
n = list(map(int,list(input())))
n.sort(reverse=True)
if n[-1] != 0 or sum(n) % 3 > 0:
    print(-1)
else: 
    print(''.join(map(str, n)))
