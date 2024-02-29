import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = [0] + list(map(int, input().rstrip().split()))
pSum = [0]

for i in range(1, n + 1):
  pSum.append(pSum[i - 1] + a[i])

for i in range(m):
  x, y = map(int, input().rstrip().split())
  print(pSum[y] - pSum[x-1])