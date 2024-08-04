def dfs(idx, v, length):
    global res
    if idx == len(S):
        res = max(res, length)
        return
    if S[idx] == '(':
        stk.append([v, length - 1])
        length = 0
    elif S[idx] == ')':
        _v, _l = stk.pop()
        length = (_v * length) + _l
    else:
        v = int(S[idx])
        length += 1
    dfs(idx + 1, v, length)


S = input()
stk = []
res = 0
dfs(0, '', 0)
print(res)