"""
시작 시간: 2023-02-09 02:56 PM
소요 시간: 10분
풀이 방법:
"""
string = input()
answer = 0
for size in range(1, len(string)+1):
    string_set = set()
    
    for j in range(len(string) + 1 - size):
        splitted = string[j:j+size]
        string_set.add(splitted)

    answer += len(string_set)

print(answer)

