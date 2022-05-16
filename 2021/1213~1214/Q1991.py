def preorder(W):
    if W == '.':
        return
    print(W, end='')
    preorder(lst[W][0])
    preorder(lst[W][1])


def inorder(W):
    if W == '.':
        return
    inorder(lst[W][0])
    print(W, end='')
    inorder(lst[W][1])


def postorder(W):
    if W == '.':
        return
    postorder(lst[W][0])
    postorder(lst[W][1])
    print(W, end='')

N = int(input())
lst = {}
for _ in range(N):
    v, l, r = input().split()
    lst[v] = [l, r]
preorder('A')
print()
inorder('A')
print()
postorder('A')






















# def preorder(value):
#     if value == '.':
#         return
#     print(value, end='')
#     preorder(tree[value][0])
#     preorder(tree[value][1])
#
#
# def inorder(value):
#     if value == '.':
#         return
#     inorder(tree[value][0])
#     print(value, end='')
#     inorder(tree[value][1])
#
#
# def postorder(value):
#     if value == '.':
#         return
#     postorder(tree[value][0])
#     postorder(tree[value][1])
#     print(value, end='')
#
#
# N = int(input())
# tree = dict()
#
# for _ in range(N):
#     v, l, r = input().split()
#     tree[v] = [l, r]
#
# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')


# 오답
# def preorder(v):
#     if v >= len(lst) or visit[v] is True or lst[v] == '.':
#         return
#     print(lst[v], end='')
#     visit[v] = True
#     preorder(v*2)
#     preorder(v*2+1)
#
#
# def inorder(v):
#     if v >= len(lst) or visit[v] is True or lst[v] == '.':
#         return
#     visit[v] = True
#     inorder(v*2)
#     print(lst[v], end='')
#     inorder(v*2+1)
#
#
# def postorder(v):
#     if v >= len(lst) or visit[v] is True or lst[v] == '.':
#         return
#     visit[v] = True
#     postorder(v * 2)
#     postorder(v * 2 + 1)
#     print(lst[v], end='')
#
#
# N = int(input())
# lst = ['.'] * ((N+1)*2)
# visit = [False] * ((N+1)*2)
# for i in range(1, N+1):
#     v, l, r = input().split()
#     if v not in lst:
#         lst[i] = v
#     if l not in lst:
#         lst[i*2] = l
#     if r not in lst:
#         lst[i*2+1] = r
#
# for i in range(1, len(lst)):
#     preorder(i)
#
# print()
# visit = [False] * ((N+1)*2)
# for i in range(1, len(lst)):
#     inorder(i)
#
# print()
# visit = [False] * ((N+1)*2)
# for i in range(1, len(lst)):
#     postorder(i)
