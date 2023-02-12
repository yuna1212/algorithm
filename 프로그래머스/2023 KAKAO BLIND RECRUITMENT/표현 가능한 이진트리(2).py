"""
시작 시간: 2023-02-12 08:16 PM
소요 시간: 1시간 40분
풀이 방법:
"""
def init_doubles():
    doubles = [0]
    number = 2
    limit = 50 
    while number <= limit:
        doubles.append(number - 1)
        number <<= 1
    doubles.append(number - 1)
    return doubles

DOUBLES = init_doubles()
print(DOUBLES)

def get_chipers(number):
    number_chiper = 0
    while number > 0:
        number >>= 1
        number_chiper += 1
    print(number_chiper)

    ans = -1
    for double in DOUBLES:
        if double >= number_chiper:
            ans = double
            break

    return double

def inspect(number, chiper):
    print('>>', str(bin(number))[2:])
    half = chiper // 2
    if half == 0:
        return 1
    print('chiper', chiper, 'half', half)
    left = number >> (half + 1)
    right = number & ((1 << half) - 1)
    print(str(bin(left))[2:], (number >> half) % 2, str(bin(right))[2:])
    if (number >> half) % 2 == 0:
        if left == 0 and right == 0:
            return 1 
        return 0 
    
    return inspect(left, half) and inspect(right, half)
    
    
def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(inspect(number, get_chipers(number)))
    return answer

print(solution([0b000101010111001]))
