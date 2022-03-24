"""
시작 시간: 2022년 3월 24일 오후 3시 10분
소요 시간: 10분
풀이 방법:
    입력을 한 글자씩 확인하여 처리함
"""
data = input()
alphabets = []
sum_number = 0
for alphabet in data:
    if "A" <= alphabet <= "Z":
        alphabets.append(alphabet)
    else:
        sum_number += int(alphabet)
alphabets.sort()
print(f'{"".join(alphabets)}{sum_number}')