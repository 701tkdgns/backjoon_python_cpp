N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
res = []
for i in range(N):
    cnt = 0
    for j in range(lst[i], lst[i] + 5):
        if j not in lst:
            cnt += 1
    res.append(cnt)
print(min(res))