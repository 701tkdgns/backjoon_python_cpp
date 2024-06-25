N, K = map(int, input().split())
medal = []
medalist = [1]
cnt, rank = 1, 1
for _ in range(N):
    lst = list(map(int, input().split()))
    medal.append(lst)
medal.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)
for i in range(1, N):
    if medal[i][1:] == medal[i - 1][1:]:
        medalist.append(rank)
        cnt += 1
    else:
        rank += cnt
        medalist.append(rank)
        cnt = 1
# print(medalist)
for i in range(N):
    if medal[i][0] == K:
        print(medalist[i])
        break
    # print(i, medal[i], medalist[i])