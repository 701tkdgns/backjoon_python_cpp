import sys
input = sys.stdin.readline
N, K = map(int, input().split())
HP = list(map(str, input().rstrip()))
visit = [False for _ in range(N)]
cnt = 0
for p_idx in range(N):
    if HP[p_idx] == "P" and not visit[p_idx]:
        for h_idx in range(p_idx-K, p_idx+K+1):
            if 0 <= h_idx < N and h_idx != p_idx and HP[h_idx] == "H" and not visit[h_idx]:
                visit[h_idx] = True
                visit[p_idx] = True
                cnt += 1
                break
print(cnt)