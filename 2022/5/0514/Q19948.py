# poem = input()
# space = int(input())
# keyboard = list(map(int, input().split()))
#
#
# def check_validity(poem, space):
#     ans = ("".join(word[0].upper() for word in poem.split()))
#     pre = poem[0]
#     if keyboard[ord(pre.upper()) - 65] - 1 < 0:
#         return print(-1)
#     else:
#         keyboard[ord(pre.upper()) - 65] -= 1
#
#     for letter in poem[1:]:
#         if pre == letter:
#             continue
#         elif letter == ' ':
#             space -= 1
#             if space < 0:
#                 return print(-1)
#             else:
#                 pre = letter
#         else:
#             if keyboard[ord(letter.upper()) - 65] - 1 < 0:
#                 return print(-1)
#             else:
#                 pre = letter
#                 keyboard[ord(letter.upper()) - 65] -= 1
#
#     pre = ans[0]
#     if keyboard[ord(pre.upper()) - 65] - 1 < 0:
#         return print(-1)
#     else:
#         keyboard[ord(pre.upper()) - 65] -= 1
#     for letter in ans[1:]:
#         if pre == letter:
#             continue
#         elif letter == ' ':
#             space -= 1
#             if space < 0:
#                 return print(-1)
#             else:
#                 pre = letter
#         else:
#             if keyboard[ord(letter.upper()) - 65] - 1 < 0:
#                 return print(-1)
#             else:
#                 pre = letter
#                 keyboard[ord(letter.upper()) - 65] -= 1
#     return print(ans)
#
#
# check_validity(poem, space)

strings = input().split()
n = int(input())
count = list(map(int, input().split()))
if len(strings) - 1 > n:
    print(-1)
    exit(0)

answer = ""
success = True
for string in strings:
    for i in range(len(string)):
        if i >= 1 and string[i] == string[i - 1]:
            continue
        if count[ord(string[i].upper()) - ord('A')] > 0:
            count[ord(string[i].upper()) - ord('A')] -= 1
        else:
            success = False
            break
    if success:
        answer += string[0].upper()
    else:
        break
if success:
    tmp = answer.lower()
    for i in range(len(tmp)):
        if i >= 1 and tmp[i] == tmp[i - 1]:
            continue
        if count[ord(tmp[i].upper()) - ord('A')] > 0:
            count[ord(tmp[i].upper()) - ord('A')] -= 1
        else:
            success = False
            break
    if success:
        print(answer)
        exit(0)
print(-1)