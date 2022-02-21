"""
시작 시간: 2022년 2월 21일 오후 9시
소요 시간: 1시간
풀이 방법:
    행렬의 결합법칙에 착안해서, 반씩 쪼개서 분할정복.
    마지막에 count가 1일때 matrix를 1000으로 나눈 나머지로 구성된 행렬을 리턴하지 않고 그냥 리턴했다가 틀림..
    그거 외엔 순조롭게 품
"""
from sys import stdin
def dataInput():
    n, count = map(int, stdin.readline().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, stdin.readline().split())))
    return matrix, count

def multiply(matrix1, matrix2):
    size = len(matrix1)
    result = []
    reverseMatrix = list(zip(*matrix2))
    for i in range(size):
        row = []
        result.append(row)
        for j in range(size):
            sum = 0
            for k in range(size):
                sum += matrix1[i][k]*reverseMatrix[j][k]
            row.append(sum%1000)
    return result

def squaring(matrix, count):
    # Base case
    if count == 1:
        for i in range(len(matrix)):
            matrix[i] = list(map(lambda x: x%1000, matrix[i]))
        return matrix
    if count == 2:
        return multiply(matrix, matrix)
    # Divide & Conquer
    if count % 2 == 0:
        partition = squaring(matrix, count/2)
        return multiply(partition, partition)
    else:
        partition = squaring(matrix, (count-1)/2)
        combine = multiply(partition, partition)
        return multiply(combine, matrix)

def solution():
    matrix, count = dataInput()
    result = squaring(matrix, count)
    for row in result:
        for element in row:
            print(element, end = " ")
        print()

solution()