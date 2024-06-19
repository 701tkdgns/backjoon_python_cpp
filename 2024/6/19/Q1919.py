f = input().rstrip()
s = input().rstrip()
F, S = {}, {}
res = 0
for a in f:
    F[a] = F.get(a, 0) + 1
for a in s:
    S[a] = S.get(a, 0) + 1
for key in F.keys():
    if S.get(key) is None:
        res += F.get(key)
    else:
        res += max(F.get(key), S.get(key)) - min(F.get(key), S.get(key))
for key in S.keys():
    if F.get(key) is None:
        res += S.get(key)
print(res)