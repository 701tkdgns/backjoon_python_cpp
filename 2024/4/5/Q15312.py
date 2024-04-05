alphabet = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = list(input().rstrip())
B = list(input().rstrip())
dp = []
for i in range(len(A)):
    dp.append(alphabet[ord(A[i])-65])
    dp.append(alphabet[ord(B[i])-65])
tmp = []
while len(dp) != 2:
    for idx in range(1, len(dp)):
        tmp.append((dp[idx] + dp[idx - 1]) % 10)
    dp = tmp
    tmp = []
print("{}{}".format(dp[0], dp[-1]))