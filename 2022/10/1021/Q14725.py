import sys
sys.setrecursionlimit(10**6)


N = int(input())
lst = []
for _ in range(N):
    tmp = list(map(str, input().split()))
    lst.append(tmp[1:])
print(lst)