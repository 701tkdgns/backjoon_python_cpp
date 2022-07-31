import sys

sys.setrecursionlimit(10 ** 6)


def dfs(k):
    lst[k] = -2
    for i in range(len(lst)):
        if lst[i] == k:
            dfs(i)


N = int(input())
lst = list(map(int, input().split()))
c = int(input())
cnt = 0
dfs(c)
for i in range(len(lst)):
    if lst[i] != -2 and i not in lst:
        cnt += 1
print(cnt)

# def dfs(k, arr):
#     arr[k] = -2
#     for i in range(len(arr)):
#         if k == arr[i]:
#             dfs(i, arr)
#
# N = int(input())
# lst = list(map(int, input().split()))
# C = int(input())
# cnt = 0
# dfs(cnt, lst)
# cnt = 0
# for i in range(len(lst)):
#     if lst[i] != -2 and i not in lst:
#         cnt += 1
# print(cnt)
