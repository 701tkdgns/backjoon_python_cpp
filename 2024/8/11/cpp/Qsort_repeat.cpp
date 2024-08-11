#include<iostream>
#include<vector>

void swap(int& a, int& b){
    int temp = a;
    a = b;
    b = temp;
};

int partition(std::vector<int>& lst, int low, int high){
    int pivot = lst[high];
    int i = low - 1;
    for (int j = low; j < high; j ++){
        if (lst[j] < pivot){
            i += 1;
            swap(lst[i], lst[j]);
        }
    }
    swap(lst[i+1], lst[high]);
    return i + 1;
}

void quickSort(std::vector<int>&lst, int low, int high){
    if(low < high){
        int pi = partition(lst, low, high);
        quickSort(lst, low, pi - 1);
        quickSort(lst, pi + 1, high);
    }
}

int main(){
    std::vector<int> lst = {5, 3, 2, 4, 1, 7, 6};
    int n = lst.size();

    quickSort(lst, 0, n - 1);

    std::cout << "Sorted array: \n";
    for (int i = 0; i < n; i++) {
        std::cout << lst[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}