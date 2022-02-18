"""
시작 시간: 2022년 2월 17일
소요 시간: 30분
풀이 방법:
    iteratable 객체에서, sort / sorted 메소드 차이 헷갈림.
    sort -> 원본 객체를 정렬
    sorted -> 정렬한 사본을 리턴
"""
def solution(answers):
    # 답안지 정리
    topStudents = []
    ansLength = len(answers)
    ansPatterns= [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    sooposAnses = []
    for p in ansPatterns:
        sooposAnses.append(ansLength//len(p)*p + p[:ansLength%len(p)])
    # 채점 scores[학생번호, 점수]
    scores = [[i+1, 0] for i in range(len(ansPatterns))]
    for sooposIdx, sooposAns in enumerate(sooposAnses):
        for i in range(len(answers)):
            if answers[i] == sooposAns[i]:
                scores[sooposIdx][1] += 1
    # 채점 결과로 학생 나열
    scores.sort(key=lambda x: -x[1])
    topStudents.append(scores[0][0])
    for i in range(1, len(scores)):
        if scores[0][1] > scores[i][1]:
            break
        topStudents.append(scores[i][0])
    sorted(topStudents)
    return topStudents
print(solution([1,3,2,4,2]))