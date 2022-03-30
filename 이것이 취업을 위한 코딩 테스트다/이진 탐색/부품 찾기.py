"""
시작 시간: 2022년 3월 30일 오전 10시 55분
소요 시간: 20분
풀이 방법:
    bs구현 -> O(NlogN + MlogM)
    근데 set 자료형 이용했다면, O(NlogN + M)
    set는 해쉬기반이어서 아이템 넣는것과 찾는 것 모두 O(1)이기 때문
    총 M개의 아이템을 set에 넣기 때문에, set 다 만드는데 O(M)시간 걸림
"""
def has(target):
    global stock
    start = 0
    end = len(stock) - 1
    while start <= end:
        mid = (start + end) // 2
        median_value = stock[mid]
        if median_value == target:
            return True
        elif median_value > target:
            end = mid - 1
        elif median_value < target:
            start = mid + 1
    return False

n = int(input())
stock = sorted(list(map(int, input().split())))
m = int(input())
needs = list(map(int, input().split()))

for target in needs:
    print("yes", end=" ") if has(target) else print("no", end=" ")