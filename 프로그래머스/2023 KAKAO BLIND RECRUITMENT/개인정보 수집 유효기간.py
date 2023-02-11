"""
시작 시간: 2023-02-11 10:08 PM
소요 시간: 40분
풀이 방법: 연, 월, 일 모두 각 배열에 담았는데, 그냥 일수로 환산해서 풀어도 괜찮음
"""
YEAR = 0; MONTH = 1; DAY = 2;
def is_expired(today, privacy_date, term):
    expired_date = [ 0, privacy_date[MONTH] + term - 1, privacy_date[DAY] ]
    expired_date[YEAR] = privacy_date[YEAR] + expired_date[MONTH] // 12
    expired_date[MONTH] = expired_date[MONTH] % 12 + 1
    # 비교
    for unit in range(3):
        if today[unit] > expired_date[unit]:
            return True
        elif today[unit] < expired_date[unit]:
            return False

    if today[DAY] == expired_date[DAY]:
        return True
    return False

def solution(today, terms, privacies):
    answer = []
    today = tuple(map(int, today.split('.')))
    terms_dict = dict()
    for term in terms:
        term = term.split()
        terms_dict[term[0]] = int(term[1])

    for i, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        date = tuple(map(int, date.split('.')))
        if is_expired(today, date, terms_dict[term_type]):
            answer.append(i+1)

    return answer
