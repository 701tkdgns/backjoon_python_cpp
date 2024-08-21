from collections import Counter
N = int(input())
lst = list(map(int, input().split()))
frequency = Counter(lst)
ans = [-1] * N
stk = []
for i in range(N - 1, -1, -1):
    while stk and frequency[lst[i]] >= frequency[stk[-1]]:
        stk.pop()
    if stk:
        ans[i] = stk[-1]
    stk.append(lst[i])
print(*ans)
