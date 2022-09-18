import sys

input = sys.stdin.readline


def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def dfs(depth):
    for node in range(N):
        if distance(location[depth], location[node]) > (location[depth][2] + location[node][2]) ** 2 or depth == node or \
                visit[node]:
            continue
        visit[node] = True
        dfs(node)


for _ in range(int(input())):
    N = int(input())
    location = []
    visit = [False for _ in range(N)]
    res = 0
    for _ in range(N):
        x, y, r = map(int, input().split())
        location.append([x, y, r])
    for i in range(N):
        if not visit[i]:
            dfs(i)
            res += 1
    print(res)

# import sys
#
# input = sys.stdin.readline
#
#
# def distance(a, b):
#     return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
#
#
# def dfs(depth):
#     for node in range(N):
#         if distance(location[depth], location[node]) > (location[depth][2] + location[node][2]) ** 2 \
#                 or depth == node or visit[node]:
#             # 2개의 노드가 있을 때 각 노드에서 정찰하는 범위보다 두 노드간 거리가 더 넓을 경우, 비교할 대상이 자기 자신, 이미 검색을 한 경우
#             continue
#         visit[node] = True
#         dfs(node)
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#     answer = 0
#     location = []
#     visit = [False for _ in range(N)]
#
#     for _ in range(N):
#         x, y, r = map(int, input().split())
#         location.append([x, y, r])
#
#     for i in range(N):
#         if not visit[i]:
#             dfs(i)
#             answer += 1
#
#     print(answer)
