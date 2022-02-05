"""
시작 시간: 2022년 2월 5일 오후 2시 30분
소요 시간: 20분
풀이 방법:
    닫는 괄호는 가장 최근에 열린 괄호여야한다는 점에서 스택을 사용함.
    함수로 구현했다면 코드가 더 깔끔하긴 했을듯
"""
bracketDict = {")": "(", "}": "{", "]": "["}
openBrackets = ["(", "{", "["]
for _ in range(int(input())):
    sentence = input()
    bracketStack = []
    for i, character in enumerate(sentence):
        if character in openBrackets:
            bracketStack.append(character)
        else:
            if bracketDict[character] == bracketStack.pop():
                if i == len(sentence) - 1:
                    if not bracketStack:
                        print("YES")
                    else:
                        print("NO")
                continue
            else:
                sentence = ""
                print("NO")
                break