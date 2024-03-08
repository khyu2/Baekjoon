import sys
input = lambda: sys.stdin.readline().rstrip()

tc = int(input())
d = [0, 1, 1, 1] + [0] * 100

for i in range(3, 101):
  d[i] = d[i-2] + d[i-3]

for _ in range(tc):
  print(d[int(input())])