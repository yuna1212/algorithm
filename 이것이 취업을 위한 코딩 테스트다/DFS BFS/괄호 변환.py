"""
시작 시간: 2022년 4월 5일 오후 1시 45분
소요 시간: 40분
풀이 방법:
    주어진 알고리즘대로 그대로 구현
    책에 잘못 잘못 적힌 부분이 있어서 헤맴,,,
    근데 DFS BFS보다는 구현쪽에 가깝지 않나..?
"""
def get_uv(s):
    open_count, close_count = 0, 0
    u, v = s, ""
    for i, c in enumerate(s):
        if c == "(":
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            u = s[0:i+1]
            v = s[i+1:]
            break
    return u, v
def is_valid(s):
    stack = []
    for c in s:
        if stack:
            last = stack[-1]
            if last == c:
                stack.append(c)
            else:
                stack.pop()
        else:
            if c == ")":
                return False
            else:
                stack.append(c)
    if stack:
        return False
    else:
        return True
def get_reversed(s):
    ret = ""
    for c in s:
        if c == "(": ret += ")"
        else: ret += "("
    return ret
def solution(p):
    if p == "" or is_valid(p):
        return p
    u, v = get_uv(p)
    if is_valid(u):
        return u + solution(v)
    return "(" + solution(v) + ")" + get_reversed(u[1:-1])