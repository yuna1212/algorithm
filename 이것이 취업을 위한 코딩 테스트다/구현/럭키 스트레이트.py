"""
시작 시간: 2022년 3월 24일 오후 2시 50분
소요 시간: 2분
풀이 방법:
    주어진 입력을 리스트로 만들어서 합을 구함
"""
# 입력
n = input()

half = len(n) // 2
left = list(map(int, list(n[:half])))
right = list(map(int, list(n[half:])))
if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")
