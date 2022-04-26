"""
시작 시간: 2022년 4월 25일 오후 10시 30분
소요 시간: 15분
풀이 방법:
    아주 간단한 구현 문제
"""
def first_competition(rank):
    if rank == 0:
        return 0
    prized_people = [1, 2, 3, 4, 5, 6]
    prize = [500, 300, 200, 50, 30, 10]
    for i in range(len(prized_people)):
        if rank <= sum(prized_people[:i+1]):
            return prize[i]
    return 0
    
def second_competition(rank):
    if rank == 0:
        return 0
    prized_people = [1, 2, 4, 8, 16]
    prize = [512, 256, 128, 64, 32]
    for i in range(len(prized_people)):
        if rank <= sum(prized_people[:i+1]):
            return prize[i]
    return 0
    
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print((first_competition(a) + second_competition(b))*10000)