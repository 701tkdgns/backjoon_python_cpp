N = int(input())
A, B = map(int, input().split())
C = int(input())
lst, res = [], 0
for _ in range(N):
    lst.append(int(input()))
lst = sorted(lst, reverse=True)
for i in range(len(lst)+1):
    price = A + B * i
    res = max(res, (C+sum(lst[:i]))//price)
print(res)
