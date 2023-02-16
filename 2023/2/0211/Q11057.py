n = int(input())
con = 10007
dp = [0 for _ in range(10 ** n + 1)]
dp[0] = 1
for i in range(1, 10 ** n):
    v = str(i)

    if len(v) == 1:
        dp[i] = 1
        continue
    chk = True
    for j in range(1, len(v)):
        if v[j] < v[j - 1]:
            chk = False
            break
    if chk:
        dp[i] = 1
print(sum(dp) % con)
