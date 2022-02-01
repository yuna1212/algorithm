"""
시작 시간: 2022년 1월 29일 오후 4시 30분
소요 시간: 1시간 30분
풀이 방법:
    알파벳을 차례로 읽으면서 w, b, x에 따라 다른 처리를 한다. 
    4글자 단위로 읽되, 글자를 가리키는 포인터를 처리한 문자 개수만큼 옮기며 읽는다.
    재귀함수의 반환값은 처리된 쿼드트리 문자열이다.
"""
def reverseQuadTree(quadTree):
    quadIndex = 0
    quadSplits = []
    for i in range(4):
        if quadIndex >= len(quadTree):
            break
        if quadTree[quadIndex] == "w" or quadTree[quadIndex] == "b":
            quadSplits.append(quadTree[quadIndex])
        else:
            quadSplits.append("x"+reverseQuadTree(quadTree[quadIndex+1:]))
        quadIndex += len(quadSplits[-1])
    
    if len(quadSplits) > 2:
      quadSplits[0:2], quadSplits[2:4] = quadSplits[2:4], quadSplits[0:2]
    return "".join(quadSplits)

for _ in range(int(input())):
    quadTree = input()
    result = reverseQuadTree(quadTree)
    print(result)