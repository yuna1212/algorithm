"""
시작 시간: 2022년 3월 22일 오후 1시
소요 시간: 5분
풀이 방법:
    매 입력에서 최솟값 확인해서 가능한 큰 값인지 확인
    큰 수 확인할 때, if문 써서 2줄 쓰는 것 보다 max(biggest_min_number, min_number)하면 더 간단
"""
n, m = map(int, input().split())
biggest_min_number = -1
for i in range(n):
    cards = map(int, input().split())
    min_number = min(cards)
    if min_number > biggest_min_number:
        biggest_min_number = min_number
print(biggest_min_number)