def dfs(idx, v, length):
    if idx == len(S):
        return length
    if S[idx] == '(':
        stk.append([v, length - 1])
        length = 0
    elif S[idx] == ')':
        _v, _length = stk.pop()
        length = (int(_v) * length) + _length
    else:
        v = S[idx]
        length += 1
    return dfs(idx + 1, v, length)


S = input()
stk = []
res = dfs(0, '', 0)
print(res)