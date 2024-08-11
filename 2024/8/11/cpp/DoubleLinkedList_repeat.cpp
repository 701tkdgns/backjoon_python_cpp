#include<iostream>

struct Node
{
    int data;
    Node *next;
    Node *prev;
    Node(int data): data(data), next(nullptr), prev(nullptr) {};
};

class DoubleLinkedList
{
private:
    /* data */
    Node* head;
public:
    DoubleLinkedList(/* args */) : head(nullptr){};
    void append(int data){
        Node*newNode=new Node(data);
        if(head==nullptr){ head=newNode; return;}
        Node*temp=head;
        while(temp->next){
            temp=temp->next;
        }
        temp->next=newNode;
        newNode->prev=temp;
        return;
    };
    void printList(){
        if (head==nullptr) return;
        Node*temp=head;
        while(temp){
            std::cout<<temp->data<< " ";
            temp=temp->next;
        }
        std::cout<<std::endl;
    }
    void printReverseList(){
        if(head==nullptr) return;
        Node*temp = head;
        while(temp->next) temp=temp->next;
        while(temp){
            std::cout<<temp->data<< " ";
            temp=temp->prev;
        }
        std::cout<<std::endl;
    }
    void deleteNode(int key){
        if(head==nullptr) return;
        Node*temp=head;
        while (temp!=nullptr && temp->data !=key) temp=temp->next;
        if(temp==nullptr) return;
        
        if(temp==head){
            head=temp->next;
            if(head!=nullptr) head->prev=nullptr;
        } else{
            if (temp->prev!=nullptr) temp->prev->next=temp->next;
            if (temp->next!=nullptr) temp->next->prev=temp->prev;
        }
        delete temp;
        
    }
    ~DoubleLinkedList(){
        Node*temp=head;
        while(temp){
            Node*next=temp->next;
            delete temp;
            temp=next;
        }
    };
};

int main(){
    DoubleLinkedList dl = DoubleLinkedList();
    dl.append(1);
    dl.printList();
    dl.append(2);
    dl.printList();
    dl.append(3);
    dl.printList();
    dl.printReverseList();
    dl.append(4);
    dl.printList();
    dl.append(5);
    dl.printList();
    dl.deleteNode(3);
    dl.printList();
    dl.printReverseList();
    
    return 0;
}