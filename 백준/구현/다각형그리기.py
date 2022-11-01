"""
시작 시간: 2022-11-01 09:40 PM
소요 시간: 2시간 20분
풀이 방법: kmp! 근데 7%에서 틀렸습니다..
"""
import sys
from collections import deque
input = sys.stdin.readline

def get_kmp_table(standard):
    n = len(standard)
    table = [0] * (n-1)
    for i in range(1, n-1):
        if standard[i] == standard[table[i-1]]:
            table[i] = table[i-1] + 1
        else:
            table[i] = 0
    return table

def kmp(standard, comparison, standard_table):
    start_index = 0
    n = len(standard)
    is_equal = False
    for i in range(n):
        is_equal = True
        if standard[start_index] != comparison[0]:
            start_index = (start_index + 1) % n
            is_equal = False
            continue
        for j in range(1, n):
            if standard[(start_index+j)%n] != comparison[j]:
                start_index = (start_index + j - standard_table[j-1]) % n
                is_equal = False
                break
        if is_equal: return True
    return False

n = int(input().strip())
standard = input().strip().split()
shapes = []
for _ in range(int(input().strip())):
    shapes.append(input().strip().split())
standard_reversed = deque() 
reversing = {'1': '3', '2': '4', '3': '1', '4': '2'}
for c in standard:
    standard_reversed.appendleft(reversing[c])
standard_table = get_kmp_table(standard)
ans = []
for shape in shapes:
    if kmp(standard, shape, standard_table) or kmp(standard_reversed, shape, standard_table):
        ans.append(' '.join(shape))

print(len(ans))
for shape in ans:
    print(shape)
