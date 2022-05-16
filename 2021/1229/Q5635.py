N = int(input())
lst = [[] for _ in range(N)]
for i in range(N):
    lst[i] = list(input().split())
lst.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(lst[len(lst)-1][0])
print(lst[0][0])