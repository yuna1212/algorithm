"""
시작 시간: 2022년 2월 15일 오후 2시 40분
소요 시간: 2시간
풀이 방법:
    처음엔 다리와 동일한 작용을 하는 리스트를 큐처럼 사용. 
    다리의 길이와 동일하며, 트럭이 없는 위치는 0, 트럭이 있는 위치는 트럭의 무게로 저장함.
    이렇게 구현했을 때 시간복잡도는 O(트럭수*다리길이).
    시간초과로 통과 못함..
    
    두번째 풀이에선 다리위에 올라가있는 트럭의 무게와, 그 트럭이 가야하는 남은 거리를 각각의 큐에 저장함.
    이때 시간복잡도는 O(트럭)
    통과
"""

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     onBridge = [0]*bridge_length
    
#     while truck_weights or sum(onBridge) > 0:
#         answer += 1
#         if not truck_weights:
#             onBridge.pop(0)
#             onBridge.append(0)
#             continue
#         next = truck_weights[0]
#         if sum(onBridge[1:]) + next <= weight:
#             onBridge.pop(0)
#             onBridge.append(next)
#             truck_weights.pop(0)
#         else:
#             onBridge.pop(0)
#             onBridge.append(0)
#     return answer
def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridge = []
    leftDist = []
    while truck_weights or sum(onBridge):
        answer += 1
        # 다리 위의 트럭들 한 칸씩 앞으로 가기
        if onBridge:
            leftDist = list(map(lambda x: x-1, leftDist))
            
            # 만약 다리의 첫 트럭이 다 건넌 상태라면 다리에서 제거
            if leftDist[0] == 0:
                onBridge.pop(0)
                leftDist.pop(0)
        
        # 새로운 트럭 올라갈 수 있다면 출발
        if truck_weights and sum(onBridge) + truck_weights[0] <= weight:
            onBridge.append(truck_weights.pop(0))
            leftDist.append(bridge_length)
        # 출발할 수 없다면 다리 위 첫번째 트럭을 다리 마지막 위치까지 이동
        elif onBridge and onBridge[0] != 1:
            move = leftDist[0] - 1
            leftDist = list(map(lambda x: x-move, leftDist))
            answer += move
    return answer


print(solution(2, 10,  [7, 4, 5, 6]))
