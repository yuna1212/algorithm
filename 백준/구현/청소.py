"""
시작 시간: 2023-02-08 08:26 PM
소요 시간: 2시간 10분
풀이 방법: 배열로 window 만들어서 풀이.. 중간 원소 빼고 더하는 것에서 문제
"""
VALUE = 0
INDEX = 1

n, k = map(int, input().split())
values = list(map(int, input().split()))
if k == 1:
    print(0)
    exit()
window = [] # (value, index)

for i in range(k):
    window.append((values[i], i))

window.sort()
answer = 0
for i in range(1, k):
    answer += abs(window[i][INDEX] - window[i-1][INDEX])

last_cost = answer
print("window", window)
print("cost", answer)

for i in range(k, n):
    new_window = [] 
    value = values[i]
    cost = last_cost

    for j in range(k):
        if window[j][INDEX] == i-k:
            print('연결 끊기!')
            if j == 0:
                cost -= abs(window[j][INDEX] - window[j+1][INDEX]) # j번째 노드 뒤의 것과 연결 끊기
            elif j == k-1:
                cost -= abs(window[j][INDEX] - window[j-1][INDEX]) # j번째 노드 앞의 것과 연결 끊기
            else:
                cost -= abs(window[j][INDEX] - window[j+1][INDEX]) # j번째 노드 뒤의 것과 연결 끊기
                cost -= abs(window[j][INDEX] - window[j-1][INDEX]) # j번째 노드 앞의 것과 연결 끊기
                cost += abs(window[j-1][INDEX] + window[j+1][INDEX]) # j-1번째 노드와 j+1번째 노드를 연결
            continue
            
        if window[j][VALUE] < value: # 앞에 끼워 넣어야 함
            cost += abs(window[j][INDEX] - i) # j번째 노드  앞에 i 노드 추가
            if len(new_window) > 0:
                cost -= abs(window[j][INDEX] - new_window[-1][INDEX]) # j 앞에 연결되어 있던 것 끊기
                cost += abs(new_window[-1][INDEX] - i) # j 앞에 연결되어 있던 것과 i 노드 연결 

            new_window.append((value, i))
        
    if len(new_window) != k:
        cost += abs(new_window[-1][INDEX] - i)
        new_window.append((value, i))

    answer = min(answer, cost)
    last_cost = cost
    window = new_window
    print("--------")
    print("window", window)
    print("cost", cost)

print(answer)



