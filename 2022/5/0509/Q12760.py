N, M = map(int, input().split())
lst = []
res = [0 for _ in range(N)]
for _ in range(N):
    tmp = sorted(list(map(int, input().split())))
    lst.append(tmp)

for i in range(M):
    tmp = []
    for v in range(N):
        tmp.append(lst[v][i])
    mx = max(tmp)
    for t in range(N):
        if mx == tmp[t]:
            res[t] += 1

tmp_mx = max(res)
answer = []
for i, v in enumerate(res):
    if tmp_mx == v:
        answer.append(i + 1)
print(*answer)