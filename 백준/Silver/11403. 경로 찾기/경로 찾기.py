import sys
import math
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [[math.inf for j in range(n)] for i in range(n)]

for i in range(n):
  for j, x in enumerate(map(int, input().split())):
    if x: a[i][j] = x

for k in range(n):
  for i in range(n):
    for j in range(n):
      a[i][j] = min(a[i][j], a[i][k] + a[k][j])

for i in range(n):
  for j in range(n):
    print(1 if a[i][j] != math.inf else 0, end=' ')
  print()