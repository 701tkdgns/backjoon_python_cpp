def dfs(x, y, visited, cnt):
    global answer
    if len(visited) == N + 1:
        answer += cnt
        return
    for idx, v in enumerate(direction):
        nx, ny = x + v[0], y + v[1]
        if (nx, ny) not in visited:
            visited.append([nx, ny])
            dfs(nx, ny, visited, cnt * probability[idx])
            visited.pop()


lst = list(map(int, input().split()))
N = lst[0]
del lst[0]
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
probability = lst
answer = 0
dfs(0, 0, [(0, 0)], 1)
print(answer * (0.01 ** N))