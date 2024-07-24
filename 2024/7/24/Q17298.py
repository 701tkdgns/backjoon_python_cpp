N = int(input())
lst = []
dp = [[[0 for _ in range(N + 1)] for _ in range(N)] for _ in range(N)]
for _ in range(N):
    tmp = list(map(int, input().split()))
    lst.append(tmp)