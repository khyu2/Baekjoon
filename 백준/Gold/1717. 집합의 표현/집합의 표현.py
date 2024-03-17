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
    if a == b: return
    self.p[a] += self.p[b]
    self.p[b] = a

  def getSize(self, n):
    return abs(self.p[n])
  
  def same_set(self, a, b):
    return self.find(a) == self.find(b)

n, m = map(int, input().split())
uf = UnionFind(n + 1)

for _ in range(m):
  cmd, a, b = map(int, input().split())
  if cmd:
    print('YES' if uf.same_set(a, b) else 'NO')
  else:
    uf.union(a, b)