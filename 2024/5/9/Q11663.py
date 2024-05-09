def dot_min(a):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def dot_max(b):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    return end


N, M = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(M):
    s, e = map(int, input().split())
    print(dot_max(e) - dot_min(s) + 1)
