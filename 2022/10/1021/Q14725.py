import sys

sys.setrecursionlimit(10 ** 6)

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        cur[0] = True


N = int(input())
lst = []
for _ in range(N):
    tmp = list(map(str, input().split()))
    lst.append(tmp[1:])
