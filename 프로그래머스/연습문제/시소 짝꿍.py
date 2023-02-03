"""
시작 시간: 2023-02-03 01:01 PM
소요 시간: 1시간 40분
풀이 방법:
"""
def solution(raw_weights):
    answer = 0

    weights = dict()

    for weight in raw_weights:
        if weight in weights:
            answer += weights[weight]
            weights[weight] += 1
        else:
            weights[weight] = 1

    tokes = dict()
    distances = (2, 3, 4)

    for distance in distances:
        for weight, count in weights.items():
            toke = distance*weight
            if toke in tokes:
                answer += tokes[toke]*count
                tokes[toke] += count
            else:
                tokes[toke] = count

    return answer

print(solution([100,180,360,100,270]))
