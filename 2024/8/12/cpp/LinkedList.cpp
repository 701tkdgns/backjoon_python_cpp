#include <iostream>
struct Node
{
    int data;
    Node *next;
    Node(int data) : data(data), next(nullptr) {};
};

class LinkedList
{
private:
    Node *head;

public:
    LinkedList() : head(nullptr) {};

    void append(int data)
    {
        Node *newNode = new Node(data);
        if (head == nullptr)
        {
            head = newNode;
            return;
        }
        Node *temp = head;
        while (temp->next){
            temp = temp->next;
        }
        temp->next = newNode;
        return;
    };

    void print()
    {
        if (head == nullptr) return;
        Node *temp = head;
        while (temp)
        {
            std::cout << temp->data << " ";
            temp=temp->next;
        }
        std::cout << std::endl;
    };

    void deleteNode(int key)
    {
        if (head == nullptr) return;
        Node *temp = head;
        Node *prev = nullptr;
        
        while(temp != nullptr && temp->data != key){
            prev = temp;
            temp=temp->next;
        }
        if (temp == nullptr) return;
        prev->next = temp->next;
        delete temp;
    }

    ~LinkedList()
    {
        Node *temp = head;
        while (temp)
        {
            Node *next = temp->next;
            delete temp;
            temp = next;
        }
    };
};

int main()
{
    LinkedList ll = LinkedList();
    ll.append(1);
    ll.print();
    ll.append(2);
    ll.print();
    ll.append(3);
    ll.print();
    ll.append(4);
    ll.print();
    ll.append(5);
    ll.print();
    ll.deleteNode(3);
    ll.print();
    ll.deleteNode(5);
    ll.print();
    return 0;
}