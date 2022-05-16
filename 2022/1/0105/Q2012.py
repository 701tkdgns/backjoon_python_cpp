import sys
N = int(sys.stdin.readline())
lst, upset = [0 for _ in range(N)], 0
for i in range(N):
    lst[i] = int(sys.stdin.readline())
lst.sort()
for i in range(1, len(lst)+1):
    upset += abs(lst[i-1] - i)
print(upset)