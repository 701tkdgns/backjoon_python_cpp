n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
res = 0
A.sort()
B.sort(key=lambda x:-x)
for i in range(n):
    res += A[i]*B[i]
print(res)