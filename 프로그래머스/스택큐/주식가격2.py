"""
시작 시간: 2022년 2월 16일 오후 9시 30분
소요 시간: 30분
풀이 방법:
    시점을 저장하는 스택을 사용해야한다는걸 타 코드에서 참고해서 품.
    처음에 while대신 if해서 통과 못했으나.. 순서도상에 빼먹은것 확인함.
    이렇게 풀면 O(N)로 해결 가능
"""
def solution(prices):
    duration = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            old = stack.pop()
            duration[old] = i - old
        stack.append(i)
    for i in stack:
        duration[i] = len(prices) - 1 - i
    return duration
print(solution([1, 2, 1, 3, 2, 1]))