// #include <iostream>
// #include <vector>
// #include <tuple>
// #include <deque>
// #include <sstream>

// using namespace std;

// int n, m;
// vector<vector<int>> graph;
// vector<vector<int>> visit;
// deque<pair<int, int>> dq;
// vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

// int bfs(){
//     int ret = -1;
//     while (!dq.empty()){
//         int x, y;
//         tie(x, y) = dq.front();
//         dq.pop_front();
//         for (auto & dir : directions){
//             int nx = dir.first + x;
//             int ny = dir.second + y;
//             if (0 <= nx && nx < n && 0 <= ny && ny < n && graph[nx][ny] != -1 && visit[nx][ny] == -1){
//                 visit[nx][ny] = visit[x][y] + 1;
//                 ret = max(visit[nx][ny], ret);
//                 dq.push_back({nx, ny});
//             } 
//         }
//     }
//     return ret;
// }

// int main()
// {
//     int res = -1;
//     cin >> n >> m;
//     graph.resize(n, vector<int>(m));
//     visit.resize(n, vector<int>(m, -1));
//     for (int i = 0;  i < n; i++){
//         string s;
//         cin >> s;
//         for (int j = 0; j < m; j++){
//             graph[i][j] = s[j] - '0';
//             if (s[j] - '0' == 1){
//                 dq.push_back({i, j});
//                 visit[i][j] = 0;
//             }
//         }
//     }
//     res = max(res, bfs());
//     cout << res << endl;
//     return 0;
// }


#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

using namespace std;

int n, m;
vector<vector<int>> lst;
vector<vector<int>> visit;
vector<pair<int, int>> direction = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
deque<pair<int, int>> dq;

void tomato() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (lst[i][j] == 1) {
                visit[i][j] = 0;
                dq.push_back({i, j});
            } else if (lst[i][j] == -1) {
                visit[i][j] = -2;
            }
        }
    }
}

void bfs() {
    while (!dq.empty()) {
        int x, y;
        tie(x, y) = dq.front();
        dq.pop_front();
        for (auto& dir : direction) {
            int nx = x + dir.first;
            int ny = y + dir.second;
            if (0 <= nx && nx < n && 0 <= ny && ny < m && visit[nx][ny] == -1 && lst[nx][ny] == 0) {
                visit[nx][ny] = visit[x][y] + 1;
                dq.push_back({nx, ny});
            }
        }
    }
}

int main() {
    cin >> m >> n; // 주의: m, n 순서 변경
    lst.resize(n, vector<int>(m));
    visit.resize(n, vector<int>(m, -1));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> lst[i][j];
        }
    }

    tomato();
    bfs();

    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visit[i][j] == -1) {
                res = -1;
                break;
            }
            res = max(res, visit[i][j]);
        }
        if (res == -1) {
            break;
        }
    }

    cout << res << endl;
    return 0;
}
