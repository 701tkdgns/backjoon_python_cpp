from collections import deque


def bfs():
    dp[1][0] = 0
    dq = deque([[1, 0]]) # 화면 이모티콘 개수, 클립보드 이모티콘 개수
    while dq:
        s, c = dq.popleft()
        if dp[s][s] == -1:
            dp[s][s] = dp[s][c] + 1
            dq.append([s, s])
        if s + c <= N and dp[s + c][c] == -1:
            dp[s + c][c] = dp[s][c] + 1
            dq.append([s + c, c])
        if s - 1 >= 0 and dp[s - 1][c] == -1:
            dp[s - 1][c] = dp[s][c] + 1
            dq.append([s - 1, c])


N = int(input())
dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
res = -1
bfs()
for i in range(N + 1):
    if dp[N][i] != -1:
        if res == -1 or res > dp[N][i]:
            res = dp[N][i]
print(res)
# https://velog.io/@aonee/%EB%B0%B1%EC%A4%80-boj-14226-%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
