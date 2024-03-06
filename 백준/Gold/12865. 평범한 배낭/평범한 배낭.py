import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
d = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
w, v = zip(*[map(int, input().split()) for _ in range(n)])
w = [0] + list(w)
v = [0] + list(v)

for i in range(1, n + 1):
  for j in range(1, k + 1):
    if j >= w[i]:
      d[i][j] = max(d[i-1][j], d[i-1][j - w[i]] + v[i])
    else:
      d[i][j] = d[i-1][j]

print(d[n][k])