"""
시작 시간: 2023-02-12 04:04 AM
소요 시간: 1시간 50분
풀이 방법:
"""
def init_doubles():
    doubles = [0]
    number = 2
    limit = 10**15
    while number <= limit:
        doubles.append(number - 1)
        number <<= 1
    return doubles

DOUBLES = init_doubles()

def get_chipers(number):
    if number == DOUBLES[1]: return 1
    elif number == DOUBLES[-1]: return len(DOUBLES) - 1
    start = 0
    end = len(DOUBLES) - 1
    middle = 0
    while True:
        middle = (start+ end) // 2
        if end - start <= 1:
            middle = end 
            break

        if DOUBLES[middle] < number:
            start = middle
        elif DOUBLES[middle] > number:
            end = middle
        else:
            break

    return middle

def inspect(number):
    if number == 1 or number == 0:
        return 1 

    chiper = get_chipers(number)
    half = chiper // 2
    left = number >> (half + 1)
    right = number % (1 << half)
    print(str(bin(left))[2:], str(bin(right))[2:])
    if (number >> half) % 2 == 0:
        if left == 0 and right == 0:
            return 1 
        return 0 
    
    return inspect(left) and inspect(right)
    
    
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(inspect(number))
    return answer

solution([63])
