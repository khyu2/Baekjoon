import sys
import math
input = lambda: sys.stdin.readline().rstrip()

def ƒ(s, e):
  if d[s][e] != math.inf: return d[s][e]
  if s == e: return 0
  if s + 1 == e:
    d[s][e] = a[s] + a[e]
    return d[s][e]
  
  for k in range(s, e + 1):
    d[s][e] = min(d[s][e], ƒ(s, k) + ƒ(k + 1, e))
  d[s][e] += ps[e] - ps[s - 1]
  return d[s][e]

for i in range(int(input())):
  n = int(input())
  a = [*map(int, input().split())]
  d = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
  ps = [a[0]] + [0 for _ in range(n)]

  for i in range(1, n):
    ps[i] = ps[i - 1] + a[i]

  print(ƒ(0, n - 1))