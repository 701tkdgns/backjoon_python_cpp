#include <iostream>
struct TreeNode
{
    int data;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int data) : data(data), left(nullptr), right(nullptr) {};
};
class BinaryTree
{
public:
    TreeNode *root;
    BinaryTree() : root(nullptr) {}
    void inorder()
    {
        inorderRec(root);
        std::cout << std::endl;
    }
    void preorder()
    {
        preorderRec(root);
        std::cout << std::endl;
    }
    void postorder()
    {
        postorderRec(root);
        std::cout << std::endl;
    }
    void insert(int value)
    {
        root = insertRec(root, value);
    }
    void deleteNode(int key)
    {
        root = deleteRec(root, key);
    }
    ~BinaryTree()
    {
        destroyTree(root);
    }

private:
    TreeNode *insertRec(TreeNode *node, int value)
    {
        if (node == nullptr)
            return new TreeNode(value);
        if (value < node->data)
            node->left = insertRec(node->left, value);
        else
            node->right = insertRec(node->right, value);
        return node;
    }
    TreeNode *deleteRec(TreeNode *node, int key)
    {
        if (node == nullptr)
            return node;
        if (key < node->data)
            node->left = deleteRec(node->left, key);
        else if (key > node->data)
            node->right = deleteRec(node->right, key);
        else
        {
            if (node->left == nullptr)
            {
                TreeNode *temp = node->right;
                delete node;
                return temp;
            }
            else if (node->right == nullptr)
            {
                TreeNode *temp = node->left;
                delete node;
                return temp;
            }
            TreeNode *temp = minValueNode(node->right);
            node->data = temp->data;
            node->right = deleteRec(node->right, temp->data);
        }
        return node;
    }
    TreeNode *minValueNode(TreeNode *node)
    {
        TreeNode *current = node;
        while (current && current->left != nullptr)
            current = current->left;
        return current;
    }
    void inorderRec(TreeNode *node)
    {
        if (node != nullptr)
        {
            inorderRec(node->left);
            std::cout << node->data << " ";
            inorderRec(node->right);
        }
        std::cout << std::endl;
    }
    void preorderRec(TreeNode *node)
    {
        if (node != nullptr)
        {
            std::cout << node->data << " ";
            preorderRec(node->left);
            preorderRec(node->right);
        }
        std::cout << std::endl;
    }
    void postorderRec(TreeNode *node)
    {
        if (node != nullptr)
        {
            postorderRec(node->left);
            postorderRec(node->right);
            std::cout << node->data << " ";
        }
        std::cout << std::endl;
    }
    void destroyTree(TreeNode *node)
    {
        if (node != nullptr)
        {
            destroyTree(node->left);
            destroyTree(node->right);
            delete node;
        }
    }
};
int main()
{
    return 0;
}