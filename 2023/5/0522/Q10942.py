import sys

input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
dp = [[0 for _ in range(N)] for _ in range(N)]
M = int(input())

for num_len in range(N):
    for start in range(N - num_len):
        end = start + num_len
        if start == end:
            dp[start][end] = 1
        elif lst[start] == lst[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1] == 1:
                dp[start][end] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])
