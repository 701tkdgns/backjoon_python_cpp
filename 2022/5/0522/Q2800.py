from itertools import combinations
lst = list(map(str, input().rstrip()))
p, idx_brs = [], []
for idx, val in enumerate(lst):
    if val == '(':
        lst[idx] = ''
        p += [idx]
    if val == ')':
        lst[idx] = ''
        idx_brs += [[p.pop(), idx]]
out = set()
for i in range(len(idx_brs)):
    for j in combinations(idx_brs, i):
        P = lst[:]
        for l, r in j:
            P[l] = '('
            P[r] = ')'
        out.add(''.join(P))
for i in sorted(out):
    print(i)
