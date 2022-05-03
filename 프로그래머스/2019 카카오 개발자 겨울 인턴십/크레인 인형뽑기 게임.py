"""
시작 시간: 2022년 5월 3일 오후 4시 45분
소요 시간: 20분
풀이 방법:
    단순 구현
"""
def solution(board, moves):
    answer = 0
    basket = []
    for crane_position in moves:
        crane_position = crane_position - 1
        doll = None
        # 인형 뽑기
        for i in range(0, len(board)):
            if board[i][crane_position]:
                doll = board[i][crane_position]
                board[i][crane_position] = 0
                break
        # 터뜨리기
        if basket and doll and basket[-1] == doll:
            basket.pop()
            answer += 2
        elif doll:
            basket.append(doll)
    return answer