k, l = map(int, input().split())
res = {}
for index in range(l):
    n = int(input())
    res[n] = index
cnt = 0
for x in sorted(res.items(), key=lambda x: x[1]):
    cnt += 1
    if cnt > k:
        break
    print(x[0])
