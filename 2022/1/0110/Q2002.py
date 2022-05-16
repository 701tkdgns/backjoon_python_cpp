# N = int(input())
# start, end = {}, []
# cnt = 0
# for i in range(1, N+1):
#     n = input()
#     start[n] = i
# for i in range(1, N+1):
#     n = input()
#     end.append(n)
# print(start)
# print(end)
# for i in range(N-1):
#     for j in range(i+1, N):
#         if start[end[i]] > start[end[j]]:
#             print('start :', start[end[i]])
#             print('end : ', start[end[j]])
#             cnt += 1
#             break
# print(cnt)

N = int(input())
start, end = {}, []
cnt = 0
for i in range(1, N + 1):
    n = input()
    start[n] = i
for i in range(1, N + 1):
    n = input()
    end.append(n)
print(start)
print(end)
for i in range(N - 1):
    for j in range(i + 1, N):
        if start[end[i]] > start[end[j]]:
            cnt += 1
            # print('start :', start[end[i]])
            # print('end : ', start[end[j]])
            break
print(cnt)