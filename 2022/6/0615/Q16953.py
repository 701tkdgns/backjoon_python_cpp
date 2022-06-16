def dp(i):
    if i == B:
        return

A, B = map(int, input().split())
lst = [0 for _ in range(A, B+1)]
