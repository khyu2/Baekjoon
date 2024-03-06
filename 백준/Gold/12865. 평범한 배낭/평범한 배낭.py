import sys
input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
w, v = zip(*(map(int, input().split()) for _ in range(n)))
d = [0] * (k + 1)

for i in range(n):
  for j in range(k, 0, -1):
    if w[i] <= j: d[j] = max(d[j], d[j - w[i]] + v[i])

print(d[k])