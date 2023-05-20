N = int(input())
A = list(map(int, input().split()))
dp = [1 for _ in range(N)]
for i in range(N):
    cnt = 0
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
sub = []
order = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == order:
        sub.append(A[i])
        order -= 1
sub.reverse()
print(*sub)
