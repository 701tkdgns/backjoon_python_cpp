def dfs(idx, arr):
    if not arr:
        return
    mn = min(arr)
    mn_idx = arr.index(mn)
    res[idx + mn_idx] = mn
    print(''.join(res))
    dfs(idx + mn_idx + 1, arr[mn_idx + 1:])
    dfs(idx, arr[:mn_idx])


S = list(input().rstrip())
res = ['' for _ in range(len(S))]
dfs(0, S)











# def dfs(idx, arr):
#     if not arr:
#         return
#     mn = min(arr)
#     mn_idx = arr.index(mn)
#     res[idx + mn_idx] = mn
#     print(''.join(res))
#     dfs(idx + mn_idx + 1, arr[mn_idx + 1:])
#     dfs(idx, arr[:mn_idx])
#
#
# S = list(input().rstrip())
# res = ['' for _ in range(len(S))]
# dfs(0, S)