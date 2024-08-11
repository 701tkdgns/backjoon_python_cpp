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

    void appendData(int data)
    {
        Node *newNode = new Node(data);
        if (head == nullptr)
        {
            head = newNode;
            return;
        }
        Node *temp = head;
        while (temp->next)
        {
            temp = temp->next;
        }
        temp->next = newNode;
        return;
    }

    void printList()
    {
        if (head == nullptr)
            return;
        Node *temp = head;
        while (temp)
        {
            std::cout << temp->data << " ";
            temp = temp->next;
        }
        std::cout << std::endl;
    }

    void deleteData(int key){
        if(head==nullptr)return;
        Node*temp=head;
        Node*prev=nullptr;
        if (temp!=nullptr && temp->data==key){
            head = temp->next;
            delete temp;
            return;
        }
        while (temp!=nullptr && temp->data!=key){
            prev=temp;
            temp=temp->next;
        }
        if (temp == nullptr) return;
        prev->next=temp->next;
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
    }
};

int main()
{
    LinkedList ll = LinkedList();
    ll.appendData(1);
    ll.printList();
    ll.appendData(2);
    ll.printList();
    ll.appendData(5);
    ll.printList();
    ll.appendData(4);
    ll.printList();
    ll.deleteData(2);
    ll.printList();

    return 0;
}