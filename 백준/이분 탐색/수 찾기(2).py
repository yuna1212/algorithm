"""
시작 시간: 2022년 2월 24일 오후 2시 15분
소요 시간: 30분
풀이 방법:
    주어진 자연수를 미리 정렬시켜두고, 찾는 수에 대해 정렬된 리스트의 반절씩 확인해가면서 탐색
    그 반절의 길이가 2가 되었을 때 하나씩 각기 탐색
    입력이 한번 주어지고 마니까 굳이 주어진 자연수들을 트리에 저장할 이유도 없음
"""
def inputData():
    input()
    treeNums = list(map(int, input().split()))
    treeNums.sort()
    input()
    targets = list(map(int, input().split()))
    return treeNums, targets

def isExisting(target, startIdx, endIdx):
    global treeNums
    if endIdx - startIdx == 1:
        if target == treeNums[startIdx] or target == treeNums[endIdx]:
            return True
        else:
            return False
    
    med = (startIdx + endIdx + 1) // 2
    if target < treeNums[med]:
        return isExisting(target, startIdx, med)
    elif target > treeNums[med]:
        return isExisting(target, med, endIdx)
    elif target == treeNums[med]:
        return True
    
def solution():
    global treeNums
    treeNums, targets = inputData()
    for t in targets:
        if isExisting(t, 0, len(treeNums)-1):
            print(1)
        else:
            print(0)

solution()