N, S = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
cnt = 0
for i in range(N-1):
    for j in range(i+1, N):
        if lst[i]+lst[j] <= S:
            cnt += 1
        else:
            break
print(cnt)
