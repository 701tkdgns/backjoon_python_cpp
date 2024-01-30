N, K = map(int, input().split())
res = []
for i in range(1, N + 1):
    if N % i == 0:
        res.append(i)
if res and len(res) >= K:
    print(res[K - 1])
else:
    print(0)