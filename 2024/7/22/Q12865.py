N, M = map(int, input().split())
bags, K = [], []
for _ in range(N):
    m, v = map(int, input().split())
    bags.append([m, v])
for _ in range(M):
    k = int(input())
    K.append(k)
