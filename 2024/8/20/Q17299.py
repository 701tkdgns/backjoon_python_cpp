import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
ans = [-1 for _ in range(N)]
frequency = Counter(lst)
stk = []
for i in range(N - 1, -1, -1):
    while stk and frequency[lst[i]] >= frequency[stk[-1]]:
        stk.pop()
    if stk:
        ans[i] = stk[-1]
    stk.append(lst[i])
print(*ans)
