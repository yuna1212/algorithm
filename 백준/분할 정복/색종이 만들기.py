"""
시작 시간: 2022년 2월 21일 오후 5시 30분
소요 시간: 1시간
풀이 방법:
    색종이를 계속 균등하게 4개씩 분할
    분할 결과, 같은 색이 나온다면 분할 중지, 색이 섞여있다면 계속 분할
"""
from sys import stdin
import itertools

def dataInputs():
    # 인풋 데이터를 받는 함수
    paper = []
    for _ in range(int(input())):
        line = list(map(int, stdin.readline().split()))
        paper.append(line)
    return paper

def findColor(piece):
    # 조각의 색깔 찾는 함수
    # return: piece가 1이면 1, 0이면 0, 섞여있으면 -1
    flatten = list(itertools.chain(*piece))
    pieceSum = sum(flatten)
    if pieceSum == len(piece)**2:
        return 1
    elif pieceSum == 0:
        return 0
    else:
        return -1
    
def slicePaper(paper):
    # 주어진 종이를 4분할 하는 함수
    n = len(paper)
    pieces = [[] for _ in range(4)]
    for i in range(int(n/2)):
        middle = int(n/2)
        pieces[0].append(paper[i][:middle])
        pieces[1].append(paper[i][middle:])
        pieces[2].append(paper[middle+i][:middle])
        pieces[3].append(paper[middle+i][middle:])
    return pieces
    
def getPiecesCount(paper):
    # return: [파란색 조각 개수, 하얀색 조각 개수]
    # Base case
    paperColor = findColor(paper)
    if paperColor == 1:
        return [1, 0]
    elif paperColor == 0:
        return [0, 1]
    
    # Divide & Conquer
    bluePieceCount = 0
    whitePieceCount = 0
    pieces = slicePaper(paper)
    for piece in pieces:
        pieceColor = findColor(piece)
        if pieceColor == 1:
            bluePieceCount += 1
        elif pieceColor == 0:
            whitePieceCount += 1
        else:
            piecesColor = getPiecesCount(piece) # 재귀
            bluePieceCount += piecesColor[0]
            whitePieceCount += piecesColor[1]
            
    return [bluePieceCount, whitePieceCount]

def solution():
    paper = dataInputs()
    result = getPiecesCount(paper)
    print(result[1])
    print(result[0])
solution()