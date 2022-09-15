import sys

input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    lst.append(int(input()))
lst.sort()
dp = [0 for _ in range(len(lst))]
dp[0] = lst[0]
for i in range(1, len(lst)):
