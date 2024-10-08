# import sys
# read = sys.stdin.readline
#
# # 아래의 Node, Trie class 구현 부분은
# # [https://alpyrithm.tistory.com/74]
# # 알파이님의 블로그를 토대로 작성했습니다.
#
# class Node(object):
#     # trie 자료구조를 위한 node
#     def __init__(self, key, data=None):
#         self.key = key
#         self.data = data
#         # dictionary 자료구조 사용
#         self.children = {}
#
# class Trie(object):
#     def __init__(self):
#         self.head = Node(None)
#
#     # 문자열 삽입
#     def insert(self, string):
#         curr_node = self.head
#         # 삽입할 string 각각의 문자에 대해 자식 Node를 만들며 내려간다.
#         for char in string:
#             # 자식 Node들 중 같은 문자가 없으면 Node 새로 생성
#             if char not in curr_node.children:
#                 curr_node.children[char] = Node(char)
#             # 같은 문자가 있으면 해당 노드로 이동
#             curr_node = curr_node.children[char]
#
#         curr_node.data = string
#
#     # 문자열이 존재하는지 search
#     def search(self, string):
#         curr_node = self.head
#
#         for char in string:
#             if char in curr_node.children:
#                 curr_node = curr_node.children[char]
#             else:
#                 return False
#
#         if curr_node.data != None:
#             return True
#
# n, m = map(int, read().split())
#
# word_trie = Trie()
# word_len = list(False for _ in range(501))
# # 주어진 문자열과 길이가 같은 문자열에 대해서만 탐색을 진행해
# # 시간복잡도 줄이기 위함
#
# for _ in range(n):
#     word = read().strip()
#     word_trie.insert(word)
#     word_len[len(word)] = True
# cnt = 0
# for _ in range(m):
#     word = read().strip()
#     if word_len[len(word)] and word_trie.search(word):
#         cnt += 1
#
# print(cnt)
from platform import node


# import string, sys
# input = sys.stdin.readline
#
# n, m = map(int, input().rstrip().split())
# words = {x: [] for x in string.ascii_lowercase}
# for _ in range(n):
#     word = input().rstrip()
#     words[word[0]].append(word)
# test = sorted([input().rstrip() for _ in range(m)])
# answer = 0
# for i in range(m):
#     for word in words[test[i][0]]:
#         if word.startswith(test[i]):
#             answer += 1
#             break
# print(answer)

# class Trie:
#
#
#     def __init__(self):
#         for i in range(27):
#             node = [Trie() for _ in range(27)]
#
#     def insert(self, string, idx):
#         if idx == len(string):
#             return
#
#         if node[ord(string[idx]) - ord('a')] is None:
#             node[string[idx]] = Trie()
#
#         node[ord(string[idx]) - ord('a')].insert(string, idx + 1)
#
#     def find(self, string, idx):
#         if idx == len(string):
#             return True
#
#         if node[ord(string[idx]) - ord('a')] is None:
#             return False
#
#         return node[ord(string[idx]) - ord('a')].find(string, idx + 1)
#
#
# n, m = map(int, input().split())
# trie = Trie()
# res = 0
# for _ in range(n):
#     s = input()
#     trie.insert(s, 0)
# for i in range(m):
#     s = input()
#     if trie.find(s, 0):
#         res += 1
# print(res)


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        test = ''
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
                test += char
            else:
                return False

        if test == string:
            return True
        else:
            return False


n, m = map(int, input().split())
S = Trie()
cnt = 0
for _ in range(n):
    S.insert(input())
for _ in range(m):
    if S.search(input()):
        cnt += 1
print(cnt)



# [https://alpyrithm.tistory.com/74]
# https://blog.hoony.me/4
# https://youseop.github.io/2020-11-09-BAEKJOON-14425_%EB%AC%B8%EC%9E%90%EC%97%B4%EC%A7%91%ED%95%A9/
