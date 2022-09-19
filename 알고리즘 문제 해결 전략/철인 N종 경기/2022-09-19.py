"""
시작 시간: 2022-09-19 08:49 PM
소요 시간: 2시간 30분
풀이 방법:
    - 책에 나온 풀이랑 접근 방식은 비슷했다.
    - 우선순위 큐를 사용하는 것에서 그치지 말고, 어떻게 그래프 만들어서 다익스트라 적용할 수 있을지 생각해보자.
        - 이 부분이 실행 시간을 가르는 중요한 포인트! 힙에서 꺼낸 아이템이 필요 없을 때 어떻게 효과적으로 처리할 수 있을까
    - 누적 거리와 누적 차이를 힙에서 꺼내 처리한 후 print 찍어보면, 중복되는 값을 포함하여 같은 누적 차이에 대한 값이 엄청 많다.
    - 하지만 동일한 누적 차이에 대해, 가장 작은 누적 거리만 필요하다. 그 외는 처리할 필요x
    - 책에서 나온 것과 같이 그래프 만들고 다익스트라 사용하면, 이 부분이 해결됨.
"""
import heapq
def input_data():
    m = int(input()) # 채택 가능한 종목의 수
    weights = []
    diffs = []
    for _ in range(m):
        weight1, weight2 = map(int, input().split())
        diffs.append(weight1 - weight2)
        weights.append(weight1)
    return weights, diffs

def is_possible(diffs):
    status = 0 
    for diff in diffs:
        if diff == 0: continue 
        if status == 0: 
            status = diff
            continue
        if status > 0 and diff < 0: return True
        if status < 0 and diff > 0: return True

    if status == 0: return True
    return False
        
def solution():
    weights, diffs = input_data()
    if not is_possible(diffs): return 'IMPOSSIBLE'
    heap = []
    for i in range(len(weights)):
        heapq.heappush(heap, (weights[i], diffs[i]))
    while heap:
        accum_weight, accum_diff = heapq.heappop(heap)
        if accum_diff == 0: return accum_weight
        for i in range(len(weights)):
            if accum_diff > 0 and diffs[i] > 0:
                continue
            if accum_diff < 0 and diffs[i] < 0:
                continue
            heapq.heappush(heap, (accum_weight+weights[i], accum_diff+diffs[i]))
        print('누적 거리', accum_weight, '누적 차이', accum_diff)

for _ in range(int(input())):
    print("답:", solution())
