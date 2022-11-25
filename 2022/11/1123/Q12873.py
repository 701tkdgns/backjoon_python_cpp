from collections import deque

N = int(input())
q = deque([i for i in range(1, N + 1)])
cnt = 1
for i in range(N -1):
    num = (cnt ** 3) % len(q)
    if num == 1:
        q.popleft()
    else:
        q.rotate(-(num - 1))
        q.popleft()
    cnt += 1
print(q.pop())

# queue =deque([i for i in range(1,7) ])

# print(queue)
# deque([1, 2, 3, 4, 5, 6])

#왼쪽에 있는 값 하나를 오른쪽으로 이동
# queue.rotate(-1)
# print(queue)
# deque([2, 3, 4, 5, 6, 1])

#오른쪽에 있는 값 하나를 왼쪽으로 이동
# queue.rotate(1)
# print(queue)
# deque([6, 1, 2, 3, 4, 5])