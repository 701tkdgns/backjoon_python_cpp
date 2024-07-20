N, K = map(int, input().split())
bags = []
for _ in range(N):
    m, v = map(int, input().split())
    bags.append([m, v])
bags.sort(key=lambda x: (x[0], -x[1]))

# https://www.acmicpc.net/problem/12865