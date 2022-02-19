"""
시작 시간: 2022년 2월 19일 오후 2시 50분
소요 시간: 2시간
풀이 방법:
    답은 맞게 나오는 것 같은데 시간초과....여전히 쓸데없이 많이 반복한다.
    이전의 모든 연산 결과에 대해 서로를 연산하고, 기존에 없는 결과 또는 N을 덜 사용한 경우는 해당 결과를 업데이트해둔다.
"""
def solution(N, number):
    answer = 9
    madeNums = []
    countN = []
    for i in range(1, 9):
        if answer < i:
            break
        # 반복하는 N으로 만든 수
        newMade = int(str(N)*i)
        if newMade not in madeNums:
            madeNums.append(newMade)
            countN.append(i)
        if newMade == number:
            answer = i
        # 이전 결과를 이용해 사칙연산
        for j in range(len(madeNums)):
            for k in range(len(madeNums)):
                count = countN[j] + countN[k]
                if count < 9:
                    newMade = madeNums[j] + madeNums[k]
                    if newMade not in madeNums:
                        madeNums.append(newMade)
                        countN.append(count)
                    elif countN[madeNums.index(newMade)] > count:
                        countN[madeNums.index(newMade)] = count
                    if newMade == number and answer > count:
                        answer = count
                            
                    newMade = madeNums[j] - madeNums[k]
                    if newMade not in madeNums:
                        madeNums.append(newMade)
                        countN.append(count)
                    elif countN[madeNums.index(newMade)] > count:
                        countN[madeNums.index(newMade)] = count
                    if newMade == number and answer > count:
                        answer = count
                        
                    newMade = madeNums[j] * madeNums[k]
                    if newMade not in madeNums:
                        madeNums.append(newMade)
                        countN.append(count)
                    elif countN[madeNums.index(newMade)] > count:
                        countN[madeNums.index(newMade)] = count
                    if newMade == number and answer > count:
                            answer = count
                        
                    if madeNums[k] != 0:
                        newMade = madeNums[j] // madeNums[k]
                        if newMade not in madeNums:
                            madeNums.append(newMade)
                            countN.append(count)
                        elif countN[madeNums.index(newMade)] > count:
                            countN[madeNums.index(newMade)] = count
                        if newMade == number and answer > count:
                                answer = count
    
    return answer if answer < 9 else -1

print(solution(5, 12))