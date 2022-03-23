"""
시작 시간: 2022년 3월 23일 오전 11시 50분
소요 시간: 5분
풀이 방법:
    1에서 0으로 변하는 지점과 0에서 1로 변하는 지점의 개수를 구해
    더 작은 것이 정답
"""
s = input()
one2zero = 0
zero2one = 0

for i in range(1, len(s)):
    last = s[i-1]
    now = s[i]
    if last != now:
        if last == "1":
            one2zero += 1
        else:
            zero2one += 1
print(min(one2zero, zero2one))