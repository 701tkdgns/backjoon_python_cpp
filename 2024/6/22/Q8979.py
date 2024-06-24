N, K = map(int, input().split())
c = []
for _ in range(N):
    lst = list(map(int, input().split()))
    c.append(lst)
c.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
Rank = [1]
rank, cnt = 1, 1
for l in range(N - 1):
    if c[l][1:] == c[l + 1][1:]:
        Rank.append(rank)
        cnt += 1
    else:
        rank += cnt
        Rank.append(rank)
        cnt = 1
res = 0
for i in range(N):
    if c[i][0] == K:
        res = i
print(Rank[res])