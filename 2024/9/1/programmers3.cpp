#include <string>
#include <vector>
#include <set>

using namespace std;

vector<vector<char>> init(int m, int n, vector<string> board){
    vector<vector<char>> boards(m, vector<char>(n));
    for (int i = 0; i < m; i++){
        for (int j = 0; j < board[i].length(); j++){
            boards[i][j] = board[i][j];
        }
    }
    return boards;
}

set<pair<int, int>> check(int m, int n, vector<vector<char>> boards){
    set<pair<int, int>> to_remove;
    for (int i = 0; i < m - 1; i++){
        for (int j = 0; j < n - 1; j ++){
            char block = boards[i][j];
            if (block != '\0' &&
                block == boards[i + 1][j] &&
                block == boards[i][j + 1] &&
                block == boards[i + 1][j + 1]){
                to_remove.insert({i, j});
                to_remove.insert({i+1, j});
                to_remove.insert({i, j+1});
                to_remove.insert({i+1, j+1});
            }
        }
    }
    return to_remove;
}

void remove_blocks(set<pair<int, int>>& to_remove, vector<vector<char>>& boards){
    for (const auto xy : to_remove){
        boards[xy.first][xy.second] = '\0';
    }
}

void drop_blocks(int m, int n, vector<vector<char>>& boards){
    for (int j = 0; j < n; j++){
        int empty_row = m - 1;
        for (int i = m - 1; i > -1; i --){
            if (boards[i][j] != '\0'){
                boards[empty_row][j] = boards[i][j];
                if (empty_row != i) boards[i][j] = '\0';
                empty_row -= 1;
            }
        }
    }
}

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    vector<vector<char>> boards = init(m, n, board);
    while (true){
        set<pair<int, int>> to_remove = check(m, n, boards);
        if (to_remove.empty()) break;
        answer += to_remove.size();
        remove_blocks(to_remove, boards);
        drop_blocks(m, n, boards);
    }
    return answer;
}