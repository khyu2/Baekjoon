import sys
input = lambda: sys.stdin.readline().rstrip()

a = input()
b = input()
n = len(a)
m = len(b)

d = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
  for j in range(m):
    if a[i] == b[j]: d[i][j] = d[i-1][j-1] + 1
    else: d[i][j] = max(d[i-1][j], d[i][j-1])

print(d[n-1][m-1])