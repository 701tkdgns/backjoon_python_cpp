N = int(input())
dp = [i for i in range(10 * 10 + 1)]
res = sum(dp[:N])
print(res)