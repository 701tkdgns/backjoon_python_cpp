from collections import deque
one = deque(map(int, input().rstrip()))
two = deque(map(int, input().rstrip()))
three = deque(map(int, input().rstrip()))
four = deque(map(int, input().rstrip()))
k = int(input())
K = []
for _ in range(k):
    idx, direct = map(int, input().split())
    K.append([idx, direct])