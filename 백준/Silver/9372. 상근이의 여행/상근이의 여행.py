import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
  n, m = map(int, input().split())
  a = [[*map(int, input().split())] for __ in range(m)]
  print(n - 1)