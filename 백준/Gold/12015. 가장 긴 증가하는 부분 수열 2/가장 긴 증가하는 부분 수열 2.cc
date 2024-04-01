#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class SegmentTree {
private:
    vector<int> tree;
    vector<pair<int, int>> a;

    int query(int node, int s, int e, int l, int r) {
        if (s > r || e < l) return 0;
        if (l <= s && e <= r) return tree[node];
        return max(query(node * 2, s, (s + e) / 2, l, r), query(node * 2 + 1, (s + e) / 2 + 1, e, l, r));
    }

    void update(int node, int s, int e, int idx, int val) {
        if (s == e) tree[node] = val;
        else {
            if (idx <= (s + e) / 2) update(node * 2, s, (s + e) / 2, idx, val);
            else update(node * 2 + 1, (s + e) / 2 + 1, e, idx, val);
            tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
        }
    }

public:
    SegmentTree(vector<pair<int, int>>& arr) : a(arr) {
        int n = arr.size();
        tree.resize(4 * n);
    }

    int query(int l, int r) {
        return query(1, 0, a.size() - 1, l, r);
    }

    void update(int idx, int val) {
        update(1, 0, a.size() - 1, idx, val);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i].second;
        a[i].first = i;
    }
    sort(a.begin(), a.end(), [](const pair<int, int>& x, const pair<int, int>& y) {
        return x.second < y.second || (x.second == y.second && x.first > y.first);
    });
    
    SegmentTree tree(a);

    vector<int> res(n);
    for (int i = 0; i < n; ++i) {
        res[i] = tree.query(0, a[i].first) + 1;
        tree.update(a[i].first, res[i]);
    }

    int max_len = *max_element(res.begin(), res.end());
    cout << max_len << endl;

    return 0;
}
