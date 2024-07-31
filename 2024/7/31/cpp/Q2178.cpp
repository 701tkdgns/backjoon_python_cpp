#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

using namespace std;

int n, m;
vector<vector<int>> maze;
vector<vector<int>> visited;
vector<vector<int>> chk;
vector<pair<int, int>> direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

void bfs(int x, int y) {
    deque<pair<int, int>> dq;
    dq.push_back({x, y});
    visited[x][y] = 1;
    while (!dq.empty()) {
        int x, y;
        tie(x, y) = dq.front();
        dq.pop_front();
        if (x == n - 1 && y == m - 1) {
            chk[x][y]++;
            break;
        }
        for (auto& dir : direction) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (0 <= nx && nx < n && 0 <= ny && ny < m && maze[nx][ny] == 1 && !visited[nx][ny]) {
                dq.push_back({nx, ny});
                visited[nx][ny] = 1;
                chk[nx][ny] = chk[x][y] + 1;
            }
        }
    }
}

int main() {
    cin >> n >> m;
    maze.resize(n, vector<int>(m));
    visited.resize(n, vector<int>(m));
    chk.resize(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        string s;
        cin >> s;
        for (int j = 0; j < m; ++j) {
            maze[i][j] = s[j] - '0';
        }
    }
    bfs(0, 0);
    cout << chk[n - 1][m - 1] << endl;
    return 0;
}
