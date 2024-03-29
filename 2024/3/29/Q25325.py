N = int(input())
A = list(input().split())
S = dict()
for i in A:
    S[i] = 0
for i in range(N):
    good = list(input().split())
    for v in good:
        S[v] = S.get(v) + 1
S = dict(sorted(S.items(), key=lambda x:(-x[1], x[0])))
for k in S.keys():
    print(k, S[k])