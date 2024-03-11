import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [int(input()) for _ in range(n)]
d = [0] * n

if n == 1:
  print(a[0])
  exit(0)

if n == 2:
  print(a[0] + a[1])
  exit(0)

d[0] = a[0]
d[1] = a[1] + a[0]
d[2] = max(d[1], max(a[0], a[1]) + a[2])
for i in range(3, n): # 현재 마시는 경우, 안 마시는 경우
  d[i] = max(d[i-1], max(d[i-3] + a[i-1], d[i-2]) + a[i])

print(max(d))