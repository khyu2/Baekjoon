import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = []
d = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
  a.append(list(map(int, input().rstrip().split())))

d[0][0] = a[0][0]
for i in range(1, n):
  for j in range(i + 1):
    d[i][j] = max(d[i-1][j-1], d[i-1][j]) + a[i][j]

print(max(d[n-1]))