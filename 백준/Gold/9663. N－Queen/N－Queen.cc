#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
using namespace std;
using ll = long long;

int vis[16], n, ans;

bool check(int row) {
    for (int i = 0; i < row; ++i) {
        if (abs(i - row) == abs(vis[i] - vis[row]) || vis[i] == vis[row]) return false;
    }
    return true;
}

void dfs(int cnt) {
    if (cnt == n) ++ans;
    else {
        for (int i = 0; i < n; ++i) {
            if (vis[cnt] == -1) {
                vis[cnt] = i;
                if (check(cnt)) dfs(cnt + 1);
                vis[cnt] = -1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    
    cin >> n;
    fill(vis, vis + 16, -1);
    
    dfs(0);
    
    cout << ans << endl;
    
    return 0;
}
