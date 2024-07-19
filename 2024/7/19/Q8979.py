N, M = map(int, input().split())
lst = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp)
lst.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
ranking = [1]
rank, cnt = 1, 1
for i in range(N - 1):
    if lst[i][1:] == lst[i + 1][1:]:
        ranking.append(rank)
        cnt += 1
    else:
        rank += cnt
        ranking.append(rank)
        cnt = 1
for i in range(N):
    if lst[i][0] == M:
        print(ranking[i])
        break
