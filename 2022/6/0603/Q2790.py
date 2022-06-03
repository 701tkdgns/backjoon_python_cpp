N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort(reverse=True)
mx = lst[-1] + N
res = 1
for i in range(1, N):
    if lst[i] + N >= mx:
        res += 1
    mx = max(mx, lst[i] + i + 1)
print(res)