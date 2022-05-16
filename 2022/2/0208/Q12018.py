n, m = map(int, input().split())
cnt = 0
tmp = []
for _ in range(n):
    P, L = map(int, input().split())
    lst = sorted(list(map(int, input().split())), reverse=True)
    if len(lst) >= L:
        tmp.append(lst[L-1])
    else:
        tmp.append(1)
tmp.sort()
for i in tmp:
    if m - i >= 0:
        m -= i
        cnt += 1
    else:
        break
print(cnt)
