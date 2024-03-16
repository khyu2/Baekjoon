import sys
import math
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [[math.inf] * n for _ in range(n)]
for _ in range(m):
  x, y, z = map(int, input().split())
  a[x-1][y-1] = z

for k in range(n):
  for i in range(n):
    for j in range(n):
      a[i][j] = min(a[i][j], a[i][k] + a[k][j])

ans = math.inf
for i in range(n):
  ans = min(ans, a[i][i])

print(ans if ans != math.inf else -1)
