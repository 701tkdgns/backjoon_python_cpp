# 플루이드 와샬
#자신이 갈 수 있는 노드들은 자기보다 작은 사람들이며
# 자신에게 오는 경로가 있는 노드들은 자기보다 큰 사람들이다.
# 이 둘의 합이 자신을 제외한 N-1인 경우 자신의 순서를 알 수 있는 것이다.
# https://claude-u.tistory.com/334

# https://www.acmicpc.net/problem/11404
# 내일 풀어보기

N, M = map(int, input().split())
lst = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    t, s = map(int, input().split())
    lst[t][s] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if lst[i][j] == 1 or (lst[i][k] == 1 and lst[k][j] == 1):
                lst[i][j] = 1

res = 0
for i in range(1, N + 1):
    known_node = 0
    for j in range(1, N + 1):
        known_node += lst[i][j] + lst[j][i]
    if known_node == N - 1:
        res += 1
print(res)