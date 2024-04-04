n = int(input())
N = list(map(int, input().split()))
nums = set(N)
K = int(input())
dp = [10e9 for _ in range(N[-1] * K + 2)]
for i in range(1, N[-1] * K + 2):
    if i in nums:
        dp[i] = 1
    else :
        for j in range(1, i // 2 + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])
    if dp[i] > K:
        s = "holsoon" if i % 2 == 0 else "jjaksoon"
        print(f"{s} win at {i}")
        break
# https://limepencil.tistory.com/19