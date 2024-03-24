import sys
input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
  def __init__(self, n):
    self.p = [-1] * n

  def find(self, n):
    if self.p[n] < 0: return n
    self.p[n] = self.find(self.p[n])
    return self.p[n]

  def union(self, a, b):
    a = self.find(a)
    b = self.find(b)
    if a == b: return False
    self.p[a] += self.p[b]
    self.p[b] = a
    return True

for _ in range(int(input())):
  n, m = map(int, input().split())
  uf = UnionFind(n + 1)
  e = []

  for __ in range(m):
    u, v = map(int, input().split())
    e.append([u, v])

  res = 0
  for u, v in e:
    if uf.union(u, v): res += 1
  
  print(res)