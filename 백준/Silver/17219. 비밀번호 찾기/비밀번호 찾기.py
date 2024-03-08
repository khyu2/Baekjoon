import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = dict(input().split() for _ in range(n))

for _ in range(m):
  print(''.join(a[input()]))