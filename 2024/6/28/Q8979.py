N, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
rankList = [1]
rank, count = 1, 1
for i in range(N - 1):
    if lst[i][1:] == lst[i + 1][1:]:
        rankList.append(rank)
        count += 1
    else:
        rank += count
        rankList.append(rank)
        count = 1
for idx in range(N):
    if lst[idx][0] == K:
        print(rankList[idx])
        break
