import sys
from collections import defaultdict


def dp(n):
    if lst[n] != 0:
        return lst[n]
    lst[n] = dp(n//P) + dp(n//Q)
    return lst[n]


if __name__ == "__main__":
    std = sys.stdin.readline()
    N, P, Q = map(int, std.split())
    lst = defaultdict(int)
    lst[0] = 1
    print(dp(N))
