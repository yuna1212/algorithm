"""
시작 시간: 2022년 2월 28일 오후 4시
소요 시간: 2시간
풀이 방법:
    그냥 전체 구간에서 이분탐색으로 최댓값을 찾으면 되는것을..
    까다롭게 생각해서 시간 더 소요함
"""
from sys import stdin
global LINES
def inputData():
    length, neededLanNumber = map(int, stdin.readline().split())
    lines = []
    for _ in range(length):
        lines.append(int(stdin.readline()))
    return neededLanNumber, lines

def countCutLines(length):
    global LINES
    count = 0
    for line in LINES:
        count += line // length
    return count

def solutoin():
    global LINES
    needed, LINES = inputData()
    minLen, maxLen = 1, max(LINES)
    midLen = (minLen+maxLen) // 2
    ans = maxLen if countCutLines(maxLen) >= needed else minLen
    
    while minLen != midLen:
        if countCutLines(midLen) >= needed:
            ans = max(ans, midLen)
            minLen = midLen
        else:
            maxLen = midLen
        midLen = (minLen+maxLen) // 2

    print(ans)
            
solutoin()
    
    
    
        
    