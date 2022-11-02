from collections import deque
def findPrime():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2*i, 10000, i):
                prime[j] = False

def bfs():
    dq = deque()
    dq.append([A, 0])
    visited = [0 for _ in range(10000)]
    visited[A] = 1

    while dq:
        now, cnt = dq.popleft()
        strNow = str(now)
        if now == B:
            return cnt
        for i in range(4):
            for j in range(10):
                tmp = int(strNow[:i] + str(j) + strNow[i+1:])
                if visited[tmp] == 0 and prime[tmp] and tmp >= 1000:
                    visited[tmp] = 1
                    dq.append([tmp, cnt + 1])


if __name__ == '__main__':
    T = int(input())
    prime = [True for _ in range(10000)]
    findPrime()
    for _ in range(T):
        A, B = map(int, input().split())
        res = bfs()
        print(res if res != None else "Impossible")