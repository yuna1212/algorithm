"""
시작 시간: 2022년 2월 6일 오전 1시
소요 시간: 50분
풀이 방법:
    여벌이 있으면서 도난당하지 않은 학생은 앞사람에게 우선 빌려준다.
    알고리즘은 금방 도출했으나, 구현중 변수 이름 잘못쓰면서 시간 지체..
"""
def solution(n, lost, reserve):
    answer = n
    reserve.sort()

    # 여분을 가지고왔으면서 도난당한 경우
    richBeggers = [x for x in reserve if x in lost ]
    reserve = [x for x in reserve if x not in richBeggers]
    lost = [x for x in lost if x not in richBeggers]
    
    # 여분 나눠주는 경우
    for rich in reserve:
        if rich-1 in lost:
            lost.remove(rich-1)
        elif rich+1 in lost:
            lost.remove(rich+1)
    return answer - len(lost)

n = 5
lost = [1, 2, 3, 5]
reserve = [2, 4]
print(solution(n, lost, reserve))