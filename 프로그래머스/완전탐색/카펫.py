"""
시작 시간: 2022년 2월 18일 오후 8시 5분
소요 시간: 20분
풀이 방법:
    방정식으로 품
    근의공식 쓰면 식이 복잡해져서 그냥 자연수 1부터 대입해서 품
"""
def solution(brown, yellow):
    s = brown+yellow
    w = 1
    h = -1
    while True:
        if brown == 2*w + 2*s/w - 4:
            h = s/w
            if h>w:
                h, w = w, h
            return [w, s/w]
        w += 1
print(solution(10, 2))