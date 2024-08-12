#include <iostream>
#include <vector>

void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
    return;
}

int partition(std::vector<int>& lst, int low, int high){
    int i = low - 1;
    int pivot = lst[high];
    for (int j = low; j < high; j++){
        if (lst[j] < pivot) {
            i += 1;
            swap(lst[i], lst[j]);
        }
    }
    swap(lst[i + 1], lst[high]);
    return i + 1;
}

void QuickSort(std::vector<int>& lst, int low, int high){
    if (low < high){
        int pivot = partition(lst, low, high);
        QuickSort(lst, low, pivot - 1);
        QuickSort(lst, pivot + 1, high);
    }
}

int main()
{
    std::vector<int> lst = {6, 3, 2, 4, 5, 1};
    int n = lst.size();
    QuickSort(lst, 0, n - 1);
    for (const int& k : lst) std::cout << k << " ";
    return 0;

}