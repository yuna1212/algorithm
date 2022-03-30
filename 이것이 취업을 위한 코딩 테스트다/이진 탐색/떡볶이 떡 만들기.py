"""
시작 시간: 2022년 3월 30일 오전 11시 30분
소요 시간: 15분
풀이 방법:
    bs 구현
"""
def get_tteok_size(slice_height):
    global origin_tteoks
    sum = 0
    for tteok in origin_tteoks:
        sub = tteok - slice_height
        if sub > 0:
            sum += sub
    return sum

n, m = map(int, input().split())
origin_tteoks = list(map(int, input().split()))

start = 0
end = max(origin_tteoks)
mid = (start + end) // 2
while start <= end:
    mid = (start + end) // 2
    client_tteok_size = get_tteok_size(mid)
    if client_tteok_size == m:
        break
    elif client_tteok_size < m:
        end = mid - 1
    else:
        start = mid + 1
        
print(mid)
    