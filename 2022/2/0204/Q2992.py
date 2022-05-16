from itertools import permutations

X = list(input().rstrip())
x = int(''.join(X))
tmp = set()
for comb in permutations(X, len(X)):
    if int(''.join(comb)) > x:
        tmp.add(int(''.join(comb)))
res = list(tmp)
res.sort()
if res:
    print(res[0])
else:
    print(0)



# import copy
#
# X = input()
# lst, L = [], len(X)
# chk = {}
# for idx in X:
#     chk[idx] = chk.get(idx, 0) + 1
# for i in range(int(X), 10**L):
#     s = ''
#     tmp = str(i)
#     t = copy.deepcopy(chk)
#     for n in range(len(tmp)):
#         if tmp[n] in X and t[tmp[n]] > 0:
#             s += tmp[n]
#             t[tmp[n]] = t.get(tmp[n]) - 1
#     if len(s) == len(X) and int(s) != int(X):
#         lst.append(int(s))
# lst.sort()
# if lst:
#     print(lst[0])
# else:
#     print(0)