def knapsack(idx, weight):
    if idx == N:
        return 0
    put = 0
    if W[idx] + weight <= K:
        put = V[idx] + knapsack(idx + 1, weight + W[idx])
    notPut = 0 + knapsack(idx + 1, weight)

    return max(put, notPut)


N, K = map(int, input().split())
W, V = [], []
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

res = knapsack(0, 0)
print(res)
