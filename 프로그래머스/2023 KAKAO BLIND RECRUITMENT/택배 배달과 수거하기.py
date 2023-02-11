"""
시작 시간: 2023-02-11 11:20 PM
소요 시간: 1시간 
풀이 방법: while문의 조건 - AND, OR 주의
"""
def carry(cap, boxes, pointer):
    # 1회 가장 먼 곳부터 배달/회수했을 때 결과 update, 먼 곳 거리와 갱신된 pointer 반환
    space = cap
    while pointer >= 0 and boxes[pointer] == 0:
        pointer -= 1

    max_distance = pointer + 1

    while pointer >= 0:
        if space >= boxes[pointer]:
            space -= boxes[pointer]
            boxes[pointer] = 0
            pointer -= 1
        else:
            boxes[pointer] -= space
            break

    return max_distance, pointer


def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_p, pickup_p = n - 1, n - 1;
    while delivery_p >= 0 or pickup_p >= 0:
        delivery_dist, delivery_p = carry(cap, deliveries, delivery_p)
        pickup_dist, pickup_p = carry(cap, pickups, pickup_p)
        answer += max(delivery_dist, pickup_dist)*2

    return answer
