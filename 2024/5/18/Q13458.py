import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split()) # b : 총, c ; 부
res = 0
for i in A:
    res += 1
    a = i - B
    if a > 0:
        res += math.ceil(a / C)
print(res)