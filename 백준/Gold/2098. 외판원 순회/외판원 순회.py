import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [[*map(int, input().split())] for _ in range(n)]
d = [[0 for _ in range(1 << n)] for _ in range(n)]

def tsp(cur, vis):
  if d[cur][vis]: return d[cur][vis]
  if vis == (1 << n) - 1 and a[cur][0]: return a[cur][0]
  ret = float('inf')

  for i in range(n):
    if not (vis & (1 << i)) and a[cur][i]:
      ret = min(ret, tsp(i, vis | (1 << i)) + a[cur][i])
  d[cur][vis] = ret
  return d[cur][vis]

print(tsp(0, 1))