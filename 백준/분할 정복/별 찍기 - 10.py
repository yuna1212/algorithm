"""
시작 시간: 2022년 5월 16일 오후 9시 15분
소요 시간: 30분
풀이 방법:
    리스트에다가 미리 저장해두고 한번에 출력
"""
def mark(row, column, n):
    # Conquer: 정 가운데 뚫기
    for i in range(row+n//3, row+2*n//3):
        for j in range(column+n//3, column+2*n//3):
            BOARD[i][j] = " "
    
    # 종결조건
    if n == 3:
        return 
    
    # Devide: 종결되지 않았으므로 재귀호출 시작
    for i in range(row, row+n, n//3):
        for j in range(column, column+n, n//3):
            if i == row+n//3 and j == column+n//3:
                continue # 정 가운데는 더이상 재귀 안해도 됨
            mark(i, j, n//3)

def print_board():
    for row in BOARD:
        for m in row:
            print(m, end="")
        print()
        
N = int(input())
BOARD = [["*"]*N for _ in range(N)]
mark(0, 0, N)
print_board()