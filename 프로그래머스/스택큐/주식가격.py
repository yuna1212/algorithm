"""
시작 시간: 2022년 2월 15일 오후 5시 30분
소요 시간: 30분
풀이 방법:
    첫번째 방법은 답은 맞지만, O(주식수^2)임.. 주어진 리스트의 길이의 제곱인 시간복잡도를 가짐.
"""
def solution(prices):
    answer = []
    while prices:
        duration = 0
        prime = prices.pop(0)
        for price in prices:
            duration += 1
            if prime > price:
                break
        answer.append(duration)
    return answer