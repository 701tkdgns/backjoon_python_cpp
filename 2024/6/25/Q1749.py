N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
dp = [[0] * (M + 1)] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, M + 1):

