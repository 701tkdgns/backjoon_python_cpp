N = int(input())
lst = list(map(int, input().split()))
stk = []
ans = [-1 for _ in range(N)]
cnt = dict()
for i in range(N):
    cnt[lst[i]] = cnt.get(lst[i], 0) + 1
for i in range(N - 1, -1, -1):
    while stk and cnt[lst[i]] >= cnt[stk[-1]]:
        stk.pop()
    if stk:
        ans[i] = stk[-1]
    stk.append(lst[i])
print(*ans)