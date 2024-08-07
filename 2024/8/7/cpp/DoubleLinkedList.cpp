#include <iostream>

struct Node {
    int data;
    Node* next;
    Node* prev;

    Node(int data) : data(data), next(nullptr), prev(nullptr) {}
};

class DoublyLinkedList {
private:
    Node* head;

public:
    DoublyLinkedList() : head(nullptr) {}

    void append(int data) {
        Node* newNode = new Node(data);
        if (!head) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
    }

    void printList() {
        Node* temp = head;
        while (temp) {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
        std::cout << std::endl;
    }

    void printListReverse() {
        if (!head) return;
        Node* temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        while (temp) {
            std::cout << temp->data << " ";
            temp = temp->prev;
        }
        std::cout << std::endl;
    }

    void deleteNode(int key) {
        Node* temp = head;

        while (temp != nullptr && temp->data != key) {
            temp = temp->next;
        }

        if (temp == nullptr) return;

        if (temp->prev) {
            temp->prev->next = temp->next;
        }
        else {
            head = temp->next;
        }

        if (temp->next) {
            temp->next->prev = temp->prev;
        }

        delete temp;
    }

    ~DoublyLinkedList() {
        Node* temp = head;
        while (temp) {
            Node* next = temp->next;
            delete temp;
            temp = next;
        }
    }
};

int main() {
    DoublyLinkedList list;

    list.append(1);
    list.append(2);
    list.append(3);

    std::cout << "Linked List: ";
    list.printList();

    std::cout << "Reversed Linked List: ";
    list.printListReverse();

    list.deleteNode(2);
    std::cout << "After deleting 2: ";
    list.printList();

    return 0;
}
