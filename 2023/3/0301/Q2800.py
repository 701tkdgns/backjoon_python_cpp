from itertools import combinations
s = list(input())
stk = []
res = set()
tmp = []
for i in range(len(s)):
    if s[i] == "(":
        stk.append(i)
    elif s[i] == ")":
        tmp.append([stk.pop(), i])

for i in range(1, len(tmp) + 1):
    c = combinations(tmp, i)
    # i개에 해당하는 조합 생성 >> nCr : len(tmp) C i
    for j in c:
        tg = list(s)
        for k in j:
            tg[k[0]], tg[k[1]] = "", ""
        res.add(''.join(tg))
for r in sorted(list(res)):
    print(r)


# 순열
# import itertools
#
# arr = ['A', 'B', 'C']
# nPr = itertools.permutations(arr, 2)
# print(list(nPr))
#
# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]


# 조합
# import itertools
#
# arr = ['A', 'B', 'C']
# nCr = itertools.combinations(arr, 2)
# print(list(nCr))
#
# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
