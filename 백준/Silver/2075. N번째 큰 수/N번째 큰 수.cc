#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> a;
int n;

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	
	cin >> n;
	a.resize(n * n);
	for (int i = 0; i < n * n; ++i) cin >> a[i];
	sort(a.begin(), a.end());
	
	cout << a[a.size() - n] << endl;
	return 0;
}