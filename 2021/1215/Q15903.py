n, m = map(int, input().split()) # 카드 갯수 n, 카드 합체 횟수 m
queue = sorted(list(map(int, input().split()))) # 합체 후 모든 값 더한 값 출력
for _ in range(m):
    a, b = queue[0], queue[1]
    for _ in range(2):
        del queue[0]
    s = a + b
    for _ in range(2):
        queue.append(s)
    queue.sort()
print(sum(queue))
