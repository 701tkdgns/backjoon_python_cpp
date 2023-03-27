from collections import deque
import sys
input = sys.stdin.readline

def path(x):
    lst = []
    tmp = x
    for _ in range(dp[x] + 1):
        lst.append(tmp)
        tmp = move[tmp]
    print(' '.join(map(str, lst[::-1])))

def bfs(v):
    dp[v] = 0
    dq = deque([])
    dq.append(v)
    while dq:
        v = dq.popleft()
        if v == K:
            print(dp[v])
            path(v)
            return dp[v]
        for new_v in [v + 1, v - 1, v * 2]:
            if 0 <= new_v < 100001 and (dp[new_v] == -1 or dp[new_v] == dp[v] + 1):
                if new_v == v * 2:
                    dq.appendleft(new_v)
                    dp[new_v] = dp[v] + 1
                    move[new_v] = v
                else:
                    dq.append(new_v)
                    dp[new_v] = dp[v] + 1
                    move[new_v] = v


N, K = map(int, input().split())
dp = [-1 for _ in range(100001)]
move = [0 for _ in range(100001)]
bfs(N)
