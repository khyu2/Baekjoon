import sys
import math
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = [[0 if i == j else math.inf for j in range(n)] for i in range(n)]

for _ in range(m):
  u, v = map(int, input().split())
  a[u-1][v-1] = a[v-1][u-1] = 1

for k in range(n):
  for i in range(n):
    for j in range(n):
      a[i][j] = min(a[i][j], a[i][k] + a[k][j])

ans = math.inf; idx = 0
for i in range(n):
  if ans > sum(a[i]):
    ans = sum(a[i])
    idx = i + 1

print(idx)
