"""
시작 시간: 2022년 1월 29일 오후 11시 30분
소요 시간: 1시간
풀이 방법:
    모든 경우의 수를 탐색한다. 스위치는 4를 주기로 결과가 반복되므로, 스위치의 모든 조합은 4^스위치 개수 이다.
    근데 코딩이 틀린듯
"""
from sys import stdin
from sys import setrecursionlimit
setrecursionlimit(1000000)

SWITCHES = [[0, 1, 2], [3, 7, 9, 11], [4, 10, 14, 15], [0, 4, 5, 6, 7], [6, 7, 8, 10, 12],
            [0, 2, 14, 15], [3, 14, 15], [4, 5, 7, 14, 15], [1, 2, 3, 4, 5], [3, 4, 5, 9, 13]]


# def countClicking(clickingCount):
#     global clocksTime
#     clockResult = clocksTime[:]
#     for i, count in enumerate(clickingCount):
#         for clockId in SWITCHES[i]:
#             clockResult = clocksTime[clockId] + count
#     clockResult = map(lambda x: x % 4, clockResult)
#     if clockResult.count(0) == len(clockResult):
#         # 12시로 맞춰진 경우
#         return sum(clocksTime)
#     else:
#         # 아닌 경우
#         return -1
def countClicking(switchClickingCount):
    global clocksTime
    global SWITCHES
    clockResult = clocksTime[:]

    # 스위치 누르기
    for switchId, count in enumerate(switchClickingCount):
        for clockId in SWITCHES[switchId]:
            clockResult[clockId] += count

    # 시간 확인
    clockResult = list(map(lambda x: x % 4, clockResult))
    if clockResult.count(0) == len(clockResult):
        # 12시로 맞춰진 경우
        return sum(clocksTime)
    else:
        # 아닌 경우
        return -1


def clocksync(switchId, switchClickCount):
    minSwitchCount = -1
    if switchId == len(switchClickCount):
        return countClicking(switchClickCount)
    for i in range(4):
        switchClickCount[switchId] = i
        nowSwitching = clocksync(switchId+1, switchClickCount[:])
        if nowSwitching >= 0:
            if minSwitchCount == -1:
                minSwitchCount = nowSwitching
            else:
                minSwitchCount = min(minSwitchCount, nowSwitching)
    return minSwitchCount


for _ in range(int(input())):
    global clocksTime
    clocksTime = list(map(lambda x: int(x)//3, stdin.readline().split()))
    print(clocksync(0, [0]*10))
