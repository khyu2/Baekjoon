#include <iostream>
#include <vector>

using namespace std;

class UnionFind {
private:
    vector<int> p;
public:
    UnionFind(int n) {
        p.resize(n + 1, -1);
    }
  
    int find(int x) {
        if (p[x] < 0) return x;
        return p[x] = find(p[x]);
    }
  
    bool merge(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return true;
        p[a] += p[b];
        p[b] = a;
        return false;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
  
    int n, m;
    cin >> n >> m;
  
    UnionFind uf(n);
  
    int idx = 0;
    for (int i = 1; i <= m; ++i) {
        int a, b;
        cin >> a >> b;
        if (uf.merge(a, b) && !idx) {
            idx = i;
        }
    }

    cout << idx << endl;

    return 0;
}
