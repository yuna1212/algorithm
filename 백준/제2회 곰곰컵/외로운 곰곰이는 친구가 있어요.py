"""
시작 시간: 2023-01-25 12:02 AM
소요 시간: 50분
풀이 방법: 시간초과
"""
import sys
input = sys.stdin.readline

def get_multiple_numbers(origin_numbers, last_numbers, upper_limit):
    ret = set()
    for origin_number in origin_numbers:
        for last_number in last_numbers:
            summed = origin_number + last_number 

            if summed <= upper_limit:
                ret.add(summed)
    return ret

def is_possible(x, y, distances):
    multiple_distances = distances
    upper_limit = max(x, y)

    while multiple_distances:
        for distance in multiple_distances:
            if x%distance == 0:
                x = 0
            if y%distance == 0:
                y = 0

        if x == 0 and y == 0:
            return True

        multiple_distances = get_multiple_numbers(distances, multiple_distances, upper_limit)

    return False

N = int(input().rstrip())
for _ in range(N):
    x, y = map(lambda x: abs(int(x)), input().rstrip().split())
    
    distances = list(map(int, input().rstrip().split()))[1:]
    if is_possible(x, y, distances):
        print("Ta-da")
    else:
        print("Gave up")
