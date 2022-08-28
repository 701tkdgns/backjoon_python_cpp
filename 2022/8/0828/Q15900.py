N = int(input())
lst = []
for _ in range(N - 1):
    a, b = map(int, input().split())
    lst.append([a, b])
print(lst)