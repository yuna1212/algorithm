"""
시작 시간: 2023-03-11 12:02 AM
소요 시간: 40분
풀이 방법:
"""
def solution(permutation):
    global N, M, numbers
    if len(permutation) == M:
        for n in permutation:
            print(n, end=" ")
        print()
        return

    for number in numbers:
        if number in permutation: continue  
        permutation.append(number)
        solution(permutation)
        permutation.pop()

    return

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

solution([])
