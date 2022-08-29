import sys

sys.setrecursionlimit(10 ** 6)
std = sys.stdin
N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, std.readline().split())
    adj[a].append(b)
    adj[b].append(a)
stk = [[1, 0]]
chk = [0 for _ in range(N + 1)]
chk[1] = -1

lst = []

while stk:
    cn, l = stk.pop()
    chk[cn] = 1

    if cn != 1 and len(adj[cn]) == 1:
        lst.append(l)
        continue

    for nn in adj[cn]:
        if chk[nn] == 0:
            stk.append([nn, l + 1])

sum_ls = sum(lst)

if sum_ls % 2:
    print("Yes")
else:
    print("No")
