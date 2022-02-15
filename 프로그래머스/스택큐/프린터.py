"""
시작 시간: 2022년 2월 15일 오전 1시 55분
소요 시간: 20분
풀이 방법:
    큐로 구현: 먼저 요청한 문서를 출력할지말지 확인하므로.
"""
def solution(priorities, location):
    answer = 0
    while True:
        popped = priorities.pop(0)
        # 문서가 하나밖에 없는 경우
        if not priorities:
            answer += 1
            break
        # 프린트
        if popped >= max(priorities):
            answer += 1
            if location == 0:
                break
            location -= 1

        # 프린트 못함
        else:
            priorities.append(popped)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

print(solution([1, 1, 9, 1, 1, 1],	0))