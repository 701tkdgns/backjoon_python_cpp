class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == '':
            return

        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp

        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                else:
                    node = node.next

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            else:
                node = node.next
