#include <bits/stdc++.h>
using namespace std;

static bool compare(pair<int, pair<int, int>> &a, pair<int, pair<int, int>> &b)
{
    if (a.first == b.first)
    {
        if (a.second.first == b.second.first) {
            return a.second.second < b.second.second;
        } else {
            return a.second.first < b.second.first;
        }
    }
    return a.first < b.first;
}

int main()
{
    int N;
    cin >> N;
    vector<vector<int>> lst(N, vector<int>(4));
    vector<pair<int, pair<int, int>>> medals(N); // Pair로 수정

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cin >> lst[i][j];
        }
    }

    for (int i = 0; i < N; i++)
    {
        int v = 1, s = 0;
        for (int j = 1; j < 4; j++)
        {
            v *= lst[i][j];
            s += lst[i][j];
        }
        medals[i] = {v, {s, lst[i][0]}}; // Pair로 수정
    }

    sort(medals.begin(), medals.end(), compare);

    for(int i = 0; i < 3; i++){
        cout << medals[i].second.second << " ";
    }
    cout << endl;

    return 0;
}
