def DP(idx):
    dp[0] = lst[0]
    for i in range(1, idx):
        dp[i] = max(lst[i], dp[i-1]*lst[i])


lst = []
for i in range(int(input())):
    lst.append(float(input()))
dp = [0 for _ in range(len(lst))]
DP(len(dp))
mx = max(dp)
print('{:.3f}'.format(mx))