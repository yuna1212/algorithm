"""
시작 시간: 2022년 3월 3일 오후 4시 50분
소요 시간: 1시간
풀이 방법:
    답(최소 게임 수)이 될수 있는 구간을 이분탐색
    구간은 0부터 20억 게임
"""
test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    r = int(m/n*100)
    start = 0
    end = 2*10**9
    mid = -1
    ans = -1
    while end - start > 1:
        mid = (start+end) // 2
        ratio = 100*(m+mid)//(n+mid)
        if  ratio >= r+1:
            # 이전 확률보다 커지면, 오른쪽 구간을 지움
            end = mid
            ans = mid
        else:
            # 이전 확률보다 작아지면, 왼쪽 구간을 지움
            start = mid
    print(ans)