"""
시작 시간: 2022년 6월 29일 오후 1시 35분
소요 시간: 10분
풀이 방법: 간단한 구현
"""
LEFT = "L"
RIGHT = "R"
def get_distance(num1, num2):
    dis = abs(num1-num2)
    return dis%3 + dis//3
def solution(numbers, hand):
    answer = ''
    left_finger = 10
    right_finger = 12
    left_keys = set([1, 4, 7])
    right_keys = set([3, 6, 9])
    for number in numbers:
        if number == 0:
            number = 11
        if number in left_keys:
            answer += "L"
            left_finger = number
        elif number in right_keys:
            answer += "R"
            right_finger = number
        else:
            left_dist = get_distance(number, left_finger)
            right_dist = get_distance(number, right_finger)
            if right_dist < left_dist:
                answer += "R"
                right_finger = number
            elif left_dist < right_dist:
                answer += "L"
                left_finger = number
            else:
                if hand[0] == "l":
                    answer += "L"
                    left_finger = number
                else:
                    answer += "R"
                    right_finger = number
    return answer