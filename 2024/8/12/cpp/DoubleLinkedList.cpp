#include<iostream>
struct Node
{
    /* data */
    int data;
    Node *next;
    Node *prev;
    Node(int data) : data(data), next(nullptr), prev(nullptr){};
};
class DoubleLinkedList{
private:
    Node *head;
public:
    DoubleLinkedList(): head(nullptr){};
    void append(int data){
        Node *newNode = new Node(data);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        Node *temp = head;
        while (temp->next){
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
    };
    void print(){
        if (head == nullptr) return;
        Node *temp = head;
        while (temp) {
            std::cout << temp->data << " ";
            temp=temp->next;
        }
        std::cout << std::endl;
    };
    void printReverse(){
        if (head == nullptr) return;
        Node *temp = head;
        while (temp->next) {
            temp = temp->next;
        }
        while (temp) {
            std::cout << temp->data << " ";
            temp = temp->prev;
        }
        std::cout << std::endl;
    };
    void deleteNode(int key){
        if (head == nullptr) return;
        Node *temp = head;
        while(temp != nullptr && temp->data != key) temp=temp->next;
        if (temp == nullptr) return;
        if (temp == head) {
            head = temp->next;
            if (head != nullptr) head->prev = nullptr;
        } else {
            if (temp->prev != nullptr) temp->prev->next = temp->next;
            if (temp->next != nullptr) temp->next->prev = temp->prev;
        }
        delete temp;
    };
    ~DoubleLinkedList(){
        Node *temp = head;
        while (temp){
            Node *next = temp->next;
            delete temp;
            temp = next;
        }
    };
};
int main(){
    DoubleLinkedList DDL = DoubleLinkedList();
    DDL.append(1);
    DDL.print();
    DDL.append(2);
    DDL.print();
    DDL.append(3);
    DDL.print();
    DDL.append(4);
    DDL.print();
    DDL.append(5);
    DDL.print();
    DDL.printReverse();
    DDL.deleteNode(3);
    DDL.print();
    DDL.printReverse();
    DDL.deleteNode(5);
    DDL.print();
    DDL.printReverse();
    DDL.deleteNode(1);
    DDL.print();
    DDL.printReverse();
    return 0;
}
