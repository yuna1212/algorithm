"""
시작 시간: 2022년 3월 10일 오후 5시 45분
소요 시간: 50분
풀이 방법:
    - N을 사용한 횟수에 따라, 나올 수 있는 모든 숫자를 저장한다. 이를 2차원 리스트에 저장
    - 핵심은 (1)2차원 리스트를 사용한 것과, (2)리스트 두개를 받아서 연산하는 메소드를 따로 분리한 것
    - 2차원 리스트를 사용함으로써 경우의 수를 더 잘 탐색할 수 있었음
        * N을 5번 사용했을 때는, N을 1번 4번, 2번 3번 연산한 결과를 다시 서로 연산한 결과임
        * 이를 인덱스로 바로 접근할 수 있었기에 빠르게 구현 가능
    - 이전에는 트리처럼 나타내서 풀이해서 안풀림
    - 표로 나타내서 해석했다면, 훨씬 빠르게 정답 접근할 수 있었을 것
"""
def solution(N, number):
    if number == N:
        return 1
    answer = 0
    results = [0, [N]]
    for n in range(2, 9):
        results.append([int(str(N)*(n))])
        for i in range(1, n//2+1):
            # i는 N의 개수
            results[-1] += operate(results[i], results[n-i])
        results[-1] = list(set(results[-1]))
        if number in results[-1]:
            answer = n
            return answer
    return -1

def operate(numbers1, numbers2):
    ret = []
    for n1 in numbers1:
        for n2 in numbers2:
            ret += [n1+n2, n1*n2]
            sub_result = max(n1-n2, n2-n1)
            if  sub_result > 0:
                ret.append(sub_result)
            if n1 != 0 and n2 != 0:
                ret.append(max(n1//n2, n2//n1))
    return ret