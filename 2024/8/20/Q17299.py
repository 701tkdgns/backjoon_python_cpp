N = int(input())
lst = list(map(int, input().split()))
ans = [-1 for _ in range(N)]
cnt = dict()
stk = []
for i in range(N):
    cnt[lst[i]] = cnt.get(lst[i], 0) + 1
for i in range(N):
    stk.append(lst[i])
print(cnt)