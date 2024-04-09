import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
d = [0 for _ in range(k + 1)]

d[0] = 1
for i in range(n):
  for j in range(a[i], k + 1):
    d[j] += d[j - a[i]]
print(d[k])