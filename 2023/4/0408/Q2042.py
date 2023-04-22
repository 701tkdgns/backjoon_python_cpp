def init(start, end, idx):
    if start == end:
        segment_tree[idx] = l[start - 1]
        return segment_tree[idx]
    # 현재 노드는 왼쪽 아래 노드와 오른쪽 아래 노드를 더한 값이다.
    mid = (start + end) // 2
    segment_tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return segment_tree[idx]


def update(start, end, idx, update_idx, update_data):
    # update 하려는 범위가 초과될 경우
    if start > update_idx or end < update_idx:
        return
    segment_tree[idx] += update_data

    # 리프노드까지 바꿔주었으면 재귀함수를 끝낸다.
    if start == end:
        return
    # 내가 관여하고 있는 노드들을 찾아서 바꿔준다 -> 재귀함수로 구현
    mid = (start + end) // 2
    update(start, mid, idx * 2, update_idx, update_data)
    update(mid + 1, end, idx * 2 + 1, update_idx, update_data)


def find_sum(start, end, idx, left, right):
    # 찾으려는 범위가 start~end 범위보다 클 경우
    if start > right or end < left:
        return 0
    # 찾으려는 범위가 segment tree 노드안에 구현되어 있을 경우
    if start >= left and end <= right:
        return segment_tree[idx]
    # 코드를 동작시키기 위한 기본 코드
    # 현재 노드는 왼쪽아래 + 오른쪽아래 노드이다.
    mid = (start + end) // 2
    sub_sum = find_sum(start, mid, idx * 2, left, right) + find_sum(mid + 1, end, idx * 2 + 1, left, right)
    return sub_sum


N, M, K = map(int, input().split())
l = [0 for _ in range(N)]
segment_tree = [0 for _ in range(N * 4)]
for i in range(N):
    l[i] = int(input())
init(1, N, 1)
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        tmp = c - l[b - 1]
        l[b - 1] = c
        update(1, N, 1, b, tmp)
    elif a == 2:
        print(find_sum(1, N, 1, b, c))
