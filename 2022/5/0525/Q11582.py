import sys
sys.setrecursionlimit(100000)


def dfs(n, a):
    if n <= 1:
        return a
    L, R = sorted(a[:n//2]), sorted(a[n//2:])
    return dfs(n//2, L) + dfs(n//2, R)


if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    k = int(input())
    print(*dfs(N, lst))