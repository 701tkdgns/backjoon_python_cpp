#include<iostream>
struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int value) : data(value), left(nullptr), right(nullptr) {}
};

class BinaryTree{
public:
    TreeNode* root;
    BinaryTree(): root(nullptr){};

    void appendNode(int data){};

    ~BinaryTree() {destroyTree(root);};
    
    void insert(int value){ root = insertRec(root, value);};

    void deleteNode(int value){root = deleteRec(root, value);};

    void inorder(){
        inorderRec(root);
        std::cout<<std::endl;
    }

    void preorder(){
        preorderRec(root);
        std::cout<<std::endl;
    }

    void postorder(){
        postorderRec(root);
        std::cout<<std::endl;
    }

private:

    TreeNode* insertRec(TreeNode* node, int value){
        if (node==nullptr) return new TreeNode(value);

        if(value < node->data) node->left = insertRec(node->left, value);
        else node->right = insertRec(node->right, value);
        
        return node;
    }

    TreeNode* deleteRec(TreeNode* node, int key){
        if(node==nullptr) return node;

        if(key < node->data) node->left = deleteRec(node->left, key);
        else if (key > node->data) node->right = deleteRec(node->right, key);
        else{
            if (node->left == nullptr) {
                TreeNode* temp = node->right;
                delete node;
                return temp;
            } else if (node->right == nullptr){
                TreeNode* temp = node->left;
                delete node;
                return temp;
            } else {
                TreeNode* temp = minvalueNode(node->right);
                node->data =  temp->data;
                node->right = deleteRec(node->right, temp->data);
            }
        }

        return node;
    }

    TreeNode* minvalueNode(TreeNode* node){
        TreeNode* current = node;
        while (current && current->left !=nullptr){
            current=current->left;
        }
        return current;
    }

    void inorderRec(TreeNode* node){
        if (node!=nullptr){
            inorderRec(node->left);
            std::cout << node->data << " ";
            inorderRec(node->right);
        }
    }

    void preorderRec(TreeNode* node){
        if (node!=nullptr){
            std::cout << node->data << " ";
            inorderRec(node->left);
            inorderRec(node->right);
        }
    }

    void postorderRec(TreeNode* node){
        if (node!=nullptr){
            inorderRec(node->left);
            inorderRec(node->right);
            std::cout << node->data << " ";
        }
    }

    void destroyTree(TreeNode* node){
        if(node !=nullptr){
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }
};

int main() {
    BinaryTree tree;
    tree.insert(50);
    tree.insert(30);
    tree.insert(20);
    tree.insert(40);
    tree.insert(70);
    tree.insert(60);
    tree.insert(80);

    std::cout << "Inorder traversal: ";
    tree.inorder();

    tree.deleteNode(20);
    std::cout << "After deleting 20: ";
    tree.inorder();

    tree.deleteNode(30);
    std::cout << "After deleting 30: ";
    tree.inorder();

    tree.deleteNode(50);
    std::cout << "After deleting 50: ";
    tree.inorder();

    return 0;
}