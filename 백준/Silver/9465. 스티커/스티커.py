import sys
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
  n = int(input().rstrip())
  a = [list(map(int, input().rstrip().split())) for _ in range(2)]
  d = [[0 for _ in range(n)] for _ in range(2)]

  d[0][0] = a[0][0]
  d[1][0] = a[1][0]
  if n != 1: d[1][1] = a[0][0] + a[1][1]
  if n != 1: d[0][1] = a[1][0] + a[0][1]
  for i in range(2, n):
    d[0][i] = max(d[1][i-1], d[0][i-2], d[1][i-2]) + a[0][i]
    d[1][i] = max(d[0][i-1], d[1][i-2], d[0][i-2]) + a[1][i]

  print(max(d[0][n-1], d[1][n-1]))
