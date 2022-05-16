from collections import defaultdict

N = int(input())
x_lst, y_lst = defaultdict(list), defaultdict(list)
res = 0
for _ in range(N):
    a, b = map(int, input().split())
    x_lst[a].append(b)
    y_lst[b].append(a)
for key in x_lst:
    if len(x_lst[key]) >= 2:
        res += 1
for key in y_lst:
    if len(y_lst[key]) >= 2:
        res += 1
print(res)