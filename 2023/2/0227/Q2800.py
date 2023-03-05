from itertools import combinations

s = list(input())
stk = []
tmp = []
for i in range(len(s)):
    if s[i] == "(":
        stk.append(i)
    if s[i] == ")":
        tmp.append([stk.pop(), i])

res = []

for i in range(1, len(tmp) + 1):
    c = combinations(tmp, i)
    for j in c:
        _s = list(s)
        for k in j:
            _s[k[0]], _s[k[1]] = '', ''
        res.append(''.join(_s))

for i in sorted(res):
    print(i)