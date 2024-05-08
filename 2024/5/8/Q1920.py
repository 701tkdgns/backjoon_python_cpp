n = int(input())
N = set(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))
for i in M:
    print(1 if i in N else 0)