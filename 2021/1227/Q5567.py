def bfs(v):
    global cnt
    queue.append([v, 0])
    check[v] = 1
    while queue:
        v, dist = queue[0][0], queue[0][1]
        del queue[0]
        if dist <= 2:
            cnt += 1
        for i in friends[v]:
            if not check[i]:
                check[i] = 1
                queue.append([i, dist+1])


n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
queue = []
for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
cnt = 0
bfs(1)
print(cnt-1)
