def knapsack(idx, weight):
    if idx == N:
        return 0
    n1 = 0
    if weight + W[idx] <= K:
        n1 = V[idx] + knapsack(idx + 1, weight + W[idx])
    n2 = 0 + knapsack(idx + 1, weight)
    return max(n1, n2)


N, K = map(int, input().split())
W, V = [], []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
print(knapsack(0, 0))
