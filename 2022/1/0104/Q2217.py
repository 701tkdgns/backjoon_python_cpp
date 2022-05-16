# N = int(input())
# rope = []
# w, cnt = 0, 0
# for i in range(N):
#     rope.append(int(input()))
# rope.sort(key=lambda x: -x)
# for i in range(N):
#     cnt += 1
#     while w // cnt < rope[i]:
#         w += 1
# print(w)

import sys

n = int(sys.stdin.readline().strip())
rope = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
mx = 0
for i in range(n):
    put = rope[i] * (n - i)
    print(rope[i] * (n - i))
    if put > mx: mx = put
print(mx)

# 로프가 한개일 때는 로프가 버틸 수 있는 한계가 최대 중량이다.
# 그럼 로프가 두개일 때는?
# 로프의 최대중량이 작은 로프의 힘 * 2 가 로프가 두개일때 최대 중량이다.
# w = min( 병렬 연결된 로프의 중량 ) * 병렬 연결된 로프의 수