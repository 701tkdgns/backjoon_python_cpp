N, S = map(str, input().split())
N = int(N)
lst = []
idx, ans = 0, ''
cnt = 0
for i in range(N):
    p, a = map(str, input().split())
    if S == p:
        idx = i
        ans = a
    lst.append([p, a])
for i in range(idx):
    if lst[i][1] == ans:
        cnt += 1
print(cnt)