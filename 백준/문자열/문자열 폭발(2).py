"""
시작 시간: 2022년 5월 11일 오후 2시
소요 시간: 30분
풀이 방법:
    KMP는 소용이 없다. 왜냐하면, '폭발 문자열은 같은 문자를 두 개 이상 포함하지 않는다'고 조건에 주어졌기 때문.
    폭탄 문자열에서 반복되는 패턴이 전혀 없기 때문에 KMP로 풀면 O(NM)이다. N은 전체 문자열 길이, M은 폭탄 문자열 길이
    
    시간복잡도를 약간 개선하기 위해 스택을 사용한다.
    끝에 문자가 동일한 경우 bomb인지 확인하도록 한다.
    
    파이썬 리스트에서 slicing 결과를 재할당하는 것 보다 del 해서 객체를 삭제하는 것이 더 효율적임을 명시
"""
def explode(string, bomb):
    bomb_size = len(bomb)
    if len(string) < bomb_size:
        return string
    stack = []
    for i in range(len(string)):
        stack.append(string[i])
        if stack[-1] == bomb[-1]:
            if "".join(stack[-bomb_size:]) == bomb:
                del stack[-bomb_size:] # stack = stack[:-bomb_size+1]보다 효율적임
    if stack:
        return "".join(stack)
    return "FRULA"
            
# 데이터 입력
sentence = input()
bomb = input()
print(explode(sentence, bomb))