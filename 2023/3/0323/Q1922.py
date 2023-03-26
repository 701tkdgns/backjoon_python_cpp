import sys

sys.setrecursionlimit(10 ** 6)


def find(a):
    if a == parent[a]:  # 자신이 루트노드면 자신을 반환
        return a
    parent[a] = find(parent[a])  # 루트노드를 찾음
    # 메모이제이션과 비슷한 아이디어
    # a의 부모를 find(parent[a])로 바꿔줌
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


N = int(input())
M = int(input())
lst = []
parent = [i for i in range(N + 1)]
res = 0
for i in range(M):
    a, b, c = map(int, input().split())
lst.sort(key=lambda x: x[0])
for dis, a, b in lst:
    if find(a) != find(b): # 루트가 같으면 할 필요가 없음
        union(a, b)
        res += dis
print(res)
