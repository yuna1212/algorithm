"""
시작 시간: 2022년 3월 22일 오후 12시 30분
소요 시간: 20분
풀이 방법:
    처음에 한번 연산한 수는 다시 연산 못하는줄 알고 풀었음,,
    5분만 더 본다면 수학적 규칙 알 수 있음 -> 반복문 사용 안하고 충분히 풀 수 있음
"""
# 입력
_, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

# 큰 수 만들기
big_number = 0
counter = 0 # 수를 몇 번 더했는지
i = 0
while True:
    number = numbers[i//2]
    if counter + k <= m:
        big_number += number*k
        counter += k
        i += 1
    else:
        big_number += number*(m-counter)
        break  
print(big_number)

# bigger = numbers[0]
# smaller = numbers[1]
# counter = m // (k+1) * k
# counter += m%(k+1)
# big_number = 0
# big_number += counter*bigger
# big_number += (m-counter)*smaller
# print(big_number)