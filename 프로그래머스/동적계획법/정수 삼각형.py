"""
시작 시간: 2022년 2월 19일 오후 5시 10분
소요 시간: 30분
풀이 방법:
    각 층에서, 각 원소가 가질 수 있는 최대 경로 값을 저장하여,
    다음 레벨에서 이전 레벨의 경로값을 가지고 다시 최댓값을 저장하는 꼴로 품.
    
    파이썬 리스트 초기화해서 풀다가 잘못 원소 추가해서 시간 소요됨..
    다음과 같이 초기화했을 때 예상하던 결과가 나오지 않음.
    maxSum = [[]]*4
    maxSum[0] = [7]
    maxSum[1] += [2]
"""
def solution(triangle):
    maxSum = []
    maxSum.append(triangle[0])
    for i in range(1, len(triangle)):
        maxSum.append([])
        for j in range(len(triangle[i])):
            leftIdx = j-1
            rightIdx = j
            sums = []
            if leftIdx >= 0:
                sums.append(maxSum[i-1][leftIdx] + triangle[i][j])
            if rightIdx < len(triangle[i-1]):
                sums.append(maxSum[i-1][rightIdx] + triangle[i][j])
            maxSum[-1].append(max(sums))
    return max(maxSum[-1])