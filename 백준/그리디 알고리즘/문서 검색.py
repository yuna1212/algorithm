"""
시작 시간: 2022-11-22 08:52 PM
소요 시간: 10분
풀이 방법: 간단한 그리디
"""
document = input()
word = input()
ans = 0
i = 0
while i < len(document) - len(word) + 1:
    is_equal = True
    for j in range(len(word)):
        if document[i+j] != word[j]:
            is_equal = False
            break
    if is_equal:
        ans += 1
        i += len(word)
    else:
        i += 1
print(ans)
