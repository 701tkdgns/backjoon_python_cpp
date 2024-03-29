N = int(input())
t = dict()
keys = []
for _ in range(N):
    mento, menti = input().split()
    if t.get(mento):
        t[mento].append(menti)
    else:
        t[mento] = [menti]
k = t.keys()
for i in k:
    keys.append(i)
keys.sort()
for _k in keys:
    t[_k].sort(reverse=True)
for _k in keys:
    for v in t[_k]:
        print(_k, v)