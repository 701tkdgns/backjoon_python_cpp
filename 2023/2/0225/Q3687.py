import sys
inf = sys.maxsize

_num = [0, 0, 1, 7, 4, 2, 0, 8, 10]
dp = [0 for _ in range(101)]

for i in range(1, 9):
    dp[i] = _num[i]
dp[6] = 6

for i in range(9, 101):
    dp[i] = dp[i-2] * 10 + _num[2]
    for j in range(3, 8):
        dp[i] = min(dp[i], dp[i-j] * 10 + _num[j])

n = int(input())
for _ in range(n):
    k = int(input())
    s, b = 0, 0
    s = dp[k]

    if k % 2 == 1:
        b = 7
        k -= 3
    while k > 0:
        b = (b*10)+1
        k -= 2
    print(s, b)