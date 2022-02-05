"""
시작 시간: 2022년 2월 4일 오후 4시
소요 시간: 2시간
풀이 방법:
    틀림. 이전 결과에 N을 사칙연산 하는 방법으로 전개.. 
    하지만 두 결과를 사칙연산 하는게 결과에 더 빠르게 도달할 수도 있음을 고려 안함.
    N = 5, number = 26인 경우, 26 = 5*5 + 5/5이나 이와 같은 경우를 반영하지 못함..
"""
def solution(N, number):
    depth = 1
    made = [N]
    while depth <= 8:
        depth += 1
        now = []
        for previous in made:
            now.append(previous - N)
            now.append(previous + N)
            now.append(previous // N)
            now.append(previous * N)
            now.append(int(str(N)*depth))
        for num in now:
            if num not in made:
                made.append(num)
        if number in now:
            return depth
    return -1

print(solution(2, 11))