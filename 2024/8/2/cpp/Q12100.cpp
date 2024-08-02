#include <bits/stdc++.h>

using namespace std;

int res = 0;
int n = 0;
vector<vector<int>> graph;

vector<vector<int>> move(int idx, vector<vector<int>> board){
    switch (idx)
    {
    case 0:
        for (int i = 0; i < n; i++){
            int top = n - 1;
            for (int j = n - 2; j > -1; j--){
                if (board[i][j] != 0){
                    int tmp = board[i][j];
                    board[i][j] = 0;
                    if (board[i][top] == 0) {
                        board[i][top] = tmp;
                    }
                    else if(board[i][top] == tmp) {
                        board[i][top] = tmp * 2;
                        top -= 1;
                    }
                    else {
                        top -= 1;
                        board[i][top] = tmp;
                    }
                }
            }
        }
        break;
    case 1:
        for (int i = 0; i < n; i++){
            int top = 0;
            for (int j = 1; j < n; j++){
                if (board[i][j] != 0) {
                    int tmp = board[i][j];
                    board[i][j] = 0;
                    if (board[i][top] == 0){
                        board[i][top] = tmp;
                    }
                    else if (board[i][top] == tmp){
                        board[i][top] = tmp * 2;
                        top += 1;
                    }
                    else {
                        top += 1;
                        board[i][top] = tmp;
                    }
                }
            }
        }
        break;
    case 2:
        for (int j = 0; j < n; j++) {
            int top = n - 1;
            for (int i = n - 2; i > -1; i--){
                if (board[i][j] != 0){
                    int tmp = board[i][j];
                    board[i][j] = 0;
                    if (board[top][j] == 0){
                        board[top][j] = tmp;
                    }
                    else if (board[top][j] == tmp){
                        board[top][j] = tmp * 2;
                        top -= 1;
                    }
                    else {
                        top -= 1;
                        board[top][j] = tmp;
                    }
                }
            }
        }
        break;
    case 3:
        for (int j = 0; j < n; j++){
            int top = 0;
            for (int i = 1; i < n; i++){
                if (board[i][j] != 0){
                    int tmp = board[i][j];
                    board[i][j] = 0;
                    if (board[top][j] == 0){
                        board[top][j] = tmp;
                    }
                    else if(board[top][j] == tmp){
                        board[top][j] = tmp * 2;
                        top += 1;
                    }
                    else
                    {
                        top += 1;
                        board[top][j] = tmp;
                    }
                }
            }
        }
        break;
    default:
        break;
    }
    return board;
}

vector<vector<int>> deep_copy(const vector<vector<int>>& original){
    vector<vector<int>> newCopy(original.size());
    for (int i = 0; i < original.size(); ++i){
        newCopy[i].resize(original[i].size());
        copy(original[i].begin(), original[i].end(), newCopy[i].begin());
    }
    return newCopy;
}

void dfs(int level, vector<vector<int>> board){
    if(level == 5){
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                res = max(res, board[i][j]);
            }
        }
        return;
    }
    for(int i = 0; i < 4; i++){
        vector<vector<int>> tmp_board = deep_copy(board);
        vector<vector<int>> move_board = move(i, tmp_board);
        dfs(level + 1, move_board);
    }

    return;
}

int main(){
    cin >> n;
    graph.resize(n, vector<int>(n));
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j ++){
            cin >> graph[i][j];
        }
    }
    dfs(0, graph);
    cout << res << endl;

    return 0;
}