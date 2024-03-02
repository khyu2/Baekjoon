import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [list(map(int, input().rstrip().split())) for _ in range(n)]
d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, n + 1):
    d[i][j] = d[i-1][j] + d[i][j-1] - d[i-1][j-1] + a[i-1][j-1]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().rstrip().split())
  print(d[x2][y2] - d[x2][y1-1] - d[x1-1][y2] + d[x1-1][y1-1])
