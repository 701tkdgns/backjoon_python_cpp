# lst = []
# for _ in range(int(input())):
#     lst.append(int(input()))
# lst.sort(reverse=True)
# mx = -1
# for i in range(len(lst)-2):
#     if lst[i] < lst[i+1] + lst[i+2]:
#         mx = max(mx, lst[i]+lst[i+1]+lst[i+2])
#         break
# print(mx)

lst = []
mx = -1
for i in range(int(input())):
    lst.append(int(input()))
lst.sort(reverse=True)
for i in range(len(lst)-2):
    if lst[i] < lst[i+1]+lst[i+2]:
        mx = lst[i]+lst[i+1]+lst[i+2]
        break
print(mx)