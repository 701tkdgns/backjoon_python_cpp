
import sys
import heapq
input = sys.stdin.readline

def main():
    global N, adj_list
    N = int(input())
    adj_list = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b, c = map(int, input().rstrip().split())
        adj_list[a].append((c, b))
        adj_list[b].append((c, a))

    pq = []
    visited = [False]*(N+1)
    pq.append((0, 1))  # 첫번째 노드에서 출발
    visited[1] = True
    while (pq):
        distance, now = heapq.heappop(pq)
        for w, next in adj_list[now]:
            if visited[next]:
                continue
            visited[next] = True
            heapq.heappush(pq, (distance+w, next))
    print(distance)
    return 0

main()