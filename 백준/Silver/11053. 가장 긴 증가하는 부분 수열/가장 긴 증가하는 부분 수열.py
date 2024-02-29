import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
d = [0] * (n + 1)

for i in range(n):
  d[i] = 1
  for j in range(i + 1):
    if a[i] > a[j] and d[i] < d[j] + 1:
      d[i] = d[j] + 1

print(max(d))