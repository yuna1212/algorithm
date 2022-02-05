"""
시작 시간: 2022년 2월 5일 오후 3시 10분
소요 시간: 40분
풀이 방법:
    연속된 신호의 합으로 K를 만들어야 하는 것에 주목하여 큐를 사용하여 풀이
"""
from sys import stdin
def makeSignals(N):
    A = [1983]
    signals = []
    for i in range(1, N+1):
        A.append((A[i-1]*214013 + 2531011) % 2**32)
        signals.append(A[i-1] % 10000 + 1)
    return signals

for _ in range(int(input())):
    K, N = map(int, stdin.readline().split())
    signals = makeSignals(N)
    kCount = 0
    signalQueue = []
    for signal in signals:
        signalQueue.append(signal)
        signalSum = sum(signalQueue)

        while(signalSum > K):
            signalSum -= signalQueue.pop(0)

        if signalSum == K:
            kCount += 1
            signalQueue.pop(0)
    print(kCount)
        
            




