"""
시작 시간: 2022년 2월 14일 오후 3시 45분
소요 시간: 
풀이 방법:
    아이디어는 책과 동일. 동심원을 그리는 것 끼리 서브트리를 구성하고 depth를 찾아 최장거리를 구하는 풀이 고안..
    그치만 구현을 못함
"""
class TreeNode:
    def __init__(self):
        self.children = []
        
logest = -1
def height(root):
    heights = []
    for child in root.children:
        heights.append(height(child))
    if not heights:
        return 0
    heights.sorted()
    if len(heights) >= 2:
        global logest
        logest = max([logest, 2 + heights[len(heights)-2], heights[len(heights) - 1]])
    return heights[-1] + 1
