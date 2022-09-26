import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

def union(x, y, idx):
    global res
    x = find(x)
    y = find(y)
    if x != y:
        parent[max(x,y)] = parent[min(x, y)]
    elif res == 0:
        res = idx

n, m = map(int, input().split())
res = 0
parent = [i for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    union(a, b, i + 1)
print(res)

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
#
# def find(x):
#     if x == parent[x]:
#         return x
#     else:
#         y = find(parent[x])
#         parent[x] = y
#         return y
#
# def union(x, y, idx):
#     global res
#     x = find(x)
#     y = find(y)
#     if x != y:
#         parent[max(x, y)] = parent[min(x, y)]
#     elif res == 0:
#         res = idx
#
#
# n, m = map(int, input().split())
# parent = [i for i in range(n)]
# res = 0
# for i in range(m):
#     a, b = map(int, input().split())
#     union(a, b, i + 1)
# print(res)
