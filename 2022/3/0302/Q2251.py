from collections import deque


def chk(x, y):
    if not visit[x][y]:
        visit[x][y] = True
        dq.append((x, y))


def bfs():
    while dq:
        x, y = dq.popleft()
        z = c - x - y

        if x == 0:
            answer.append(z)

        # x -> y
        water = min(x, b - y)
        chk(x - water, y + water)
        # x -> z
        water = min(x, c - z)
        chk(x - water, y)
        # y -> x
        water = min(y, a - x)
        chk(x + water, y - water)
        # y -> z
        water = min(y, c - z)
        chk(x, y - water)
        # z -> x
        water = min(z, a - x)
        chk(x + water, y)
        # z -> y
        water = min(z, b - y)
        chk(x, y + water)


a, b, c = map(int, input().split())
visit = [[False for _ in range(201)] for _ in range(201)]
visit[0][0] = True
dq = deque()
dq.append((0, 0))
answer = []
bfs()
answer.sort()
print(' '.join(map(str, answer)))
# 물을 옮기는 방법의 수를 찾는다.
# x -> y, x -> z, y -> x, y -> z, z -> x, z -> y : 6가지
# water = min(x, b - y) : x에서 y로 옮길 물. x 전체를 옮기거나 b물통을 꽉 채우는 방법이 있다.
# pour(x - water, y + water) : 옮긴 후의 x와 y의 상태를 큐에 저장한다.
# c물통에 남아있는 물의 양은
# z = c - x - y
# visited로 (x, y)경우의 수에 대한 중복을 방지한다.
# https://cijbest.tistory.com/14
