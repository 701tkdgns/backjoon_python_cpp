N = int(input())
lst = [[] for _ in range(N)]
visit = [[False] for _ in range(N)]
for _ in range(N):
    lst.append(list(map(str, input().rstrip())))