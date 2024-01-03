# https://blog.naver.com/leeinje66/221622228795
# https://c4u-rdav.tistory.com/22

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setValue(self, value):
        self.value = value

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value


class BinarySearchTree:
    def __init__(self):
        self.head = None

    def search(self, value):
        if self.head is None:
            return False, None

        depth = 0
        node = self.head

        while node:
            if value == node.getValue():
                return True, depth
            else:
                if value < node.getValue():
                    node = node.getLeft()
                else:
                    node = node.getRight()
            depth += 1
        return False, None

    def show(self, node, option):
        if node is None:
            return
        if option == 1:
            print(node.value, end=' ')
            self.show(node.getLeft(), option)
            self.show(node.getRight(), option)
        elif option == 2:
            self.show(node.getLeft(), option)
            print(node.value, end=' ')
            self.show(node.getRight(), option)
        else:
            self.show(node.getLeft(), option)
            self.show(node.getRight(), option)
            print(node.value, end=' ')

    def print_tree(self, option):
        if option == 1:
            print('preoder:', end=' ')
        elif option == 2:
            print('inorder:', end=' ')
        else:
            print('postorder:', end=' ')
        self.show(self.head, option)
        print()

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while True:
                if value < node.getValue():
                    if node.getLeft() is None:
                        node.setLeft(Node(value))
                        break
                    else:
                        node = node.left
                else:
                    if node.getRight() is None:
                        node.setRight(Node(value))
                        break
                    else:
                        node = node.right

    def delete(self, value):
        if self.head is None:
            return False

        node = self.head
        parent = self.head
        check = False

        while node:
            if value == node.getValue():
                check = True
                break
            else:
                parent = node
                if value < node.getValue():
                    node = node.getLeft()
                else:
                    node = node.getRight()

        if not check:
            return False

        if node.getLeft() is None and node.getRight() is None:
            if value < parent.getValue():
                parent.setLeft(None)
            else:
                parent.setRight(None)

        elif node.getLeft() and node.getRight() is None:
            if value < parent.getValue():
                parent.setLeft(node.getLeft())
            else:
                parent.setRight(node.getLeft())

        elif node.getLeft() is None and node.getRight():
            if value < parent.getValue():
                parent.setLeft(node.getRight())
            else:
                parent.setRight(node.getRight())

        elif node.getLeft() and node.getRight():
            current, child = node, node.getRight()
            while child.getLeft():
                current, child = child, child.getLeft()
            node.setValue(child.getValue())
            if current != node:
                if child.getRight():
                    current.setLeft(child.getRight())
                else:
                    current.setLeft(None)
            else:
                node.setRight(child.getRight())
        return True


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(6)
    bst.insert(3)
    bst.insert(8)
    bst.insert(5)
    bst.insert(1)
    bst.insert(7)
    bst.insert(9)
    bst.print_tree(1)
    bst.print_tree(2)
    bst.print_tree(3)

    v = 7
    r = bst.search(v)

    if r[0]:
        print('depth of', str(v) + ":", r[1])
    else:
        print('There is no', v)

    v = 6
    if r:
        print(v, 'is deleted')
    else:
        print('There in no', v)
    bst.print_tree()