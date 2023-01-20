"""
시작 시간: 2023-01-20 05:20 PM
소요 시간: 30분
풀이 방법:
"""
def solution(input_string):
    answer = ''
    appeared_counter = dict()
    previous = input_string[0]
    appeared_counter[previous] = 1
    for i in range(1, len(input_string)):
        now = input_string[i]
        if(previous == now): continue

        previous = now

        if now in appeared_counter:
            if appeared_counter[now] == 1:
                appeared_counter[now] += 1
            continue

        appeared_counter[now] = 1

    alone_alphabets = list(filter(lambda k: appeared_counter[k] > 1, appeared_counter.keys()))
    if(alone_alphabets):
        alone_alphabets.sort()
        return ''.join(alone_alphabets)
    return 'N'

print(solution(input()))
