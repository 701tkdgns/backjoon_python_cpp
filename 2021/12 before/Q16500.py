def sol(idx):
    global res
    if idx == len(S):
        res = 1
        return
    if dp[idx]:
        return
    dp[idx] = 1

    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]):
            for j in range(len(A[i])):
                if A[i][j] != S[idx+j]:
                    break
                else:
                    sol(idx+len(A[i]))


S, A = input(), []
dp = [0] * 101
N = int(input())
for _ in range(N):
    A.append(input())
res = 0
sol(0)
print(res)
