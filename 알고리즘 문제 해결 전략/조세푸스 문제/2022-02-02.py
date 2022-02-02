"""
시작 시간: 2022년 2월 2일 오후 3시 30분
소요 시간: 1시간
풀이 방법:
    양방향 원형 링크드리스트를 만들었다.
    근데 더 좋은 방법 있음!
"""
import copy
from sys import stdin
class Soldier:
    def __init__(self, name, previousNode, nextNode):
        self.name = name
        self.previousNode = previousNode
        self.nextNode = nextNode

    def getNextSuicider(self, interval):
        returnNode = self
        for i in range(interval):
            returnNode = returnNode.nextNode
        return returnNode

def connectSoldier(soldier):
    soldier.previousNode.nextNode = soldier.nextNode
    soldier.nextNode.previousNode = soldier.previousNode

for _ in range(int(input())):
    numberOfPeople, suicideInterval = map(int, stdin.readline().split())
    print(numberOfPeople, suicideInterval)
    # 링크드리스트 생성
    starter = Soldier(1, None, None)
    personAdded = starter
    for i in range(1, numberOfPeople - 1):
        personAdded.nextNode = Soldier(i+1, personAdded, None)
        personAdded = personAdded.nextNode
    personAdded.nextNode = Soldier(numberOfPeople - 1, personAdded, starter)
    personAdded = personAdded.nextNode
    starter.previousNode = personAdded

    # 자살 시작
    while numberOfPeople > 2:
        connectSoldier(starter)
        starter = starter.getNextSuicider(suicideInterval)
        numberOfPeople -= 1
    for _ in range(2):
        print(">>> ", starter.name)
        starter = starter.nextNode



