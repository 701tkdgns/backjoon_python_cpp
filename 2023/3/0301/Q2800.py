from itertools import combinations
s = list(input())
stk = []
tmp = []
res = set()
for idx, word in enumerate(s):
    if word == "(":
        stk.append(idx)
    elif word == ")":
        tmp.append([stk.pop(), idx])

# 괄호끼리 인덱스를 tmp 리스트에 저장함

for i in range(1, len(tmp) + 1):
    c = combinations(tmp, i)
    #
    for j in c:
        tg = list(s)
        for k in j:
            tg[k[0]], tg[k[1]] = '', ''
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