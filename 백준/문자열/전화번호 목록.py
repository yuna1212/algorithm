"""
시작 시간: 2022-10-19 03:47 PM
소요 시간: 20분
풀이 방법: 모든 string 비교하면서 O(N^2)으로 푸니까 시간초과
"""
import sys
input = sys.stdin.readline
def is_included(str1, str2):
    smaller = str1
    bigger = str2
    if len(str1) > len(str2):
        smaller = str2
        bigger = str1
    for i in range(len(smaller)):
        if smaller[i] != bigger[i]: return False
    return True

def is_consistent(strings):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_included(strings[i], strings[j]):
                return False
    return True

for _ in range(int(input().strip())):
    n = int(input().strip())
    strings = []
    for _ in range(n):
        strings.append(input().strip())
    if is_consistent(strings):
        print("YES")
    else:
        print("NO")

