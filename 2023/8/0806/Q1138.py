N = int(input())
lst = list(map(int, input().split()))
visit = [0] * N
for i in range(N):
    cnt = 0
    for j in range(N):
        if cnt == lst[i] and visit[j] == 0:
            visit[j] = i + 1
            break
        elif visit[j] == 0:
            cnt += 1
    print(visit)