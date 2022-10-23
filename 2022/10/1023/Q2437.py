N = int(input())
lst = list(map(int, input().split()))
lst.sort()

cnt, res = 0, 0
for i in range(N - 1):
    cnt += lst[i]
    if cnt + 1 < lst[i + 1]:
        res = cnt + 1
        break

if lst[0] > 1:
    res = 1
elif res == 0:
    res = cnt + lst[N - 1] + 1
print(res)