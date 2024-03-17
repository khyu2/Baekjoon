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

n, m = map(int, input().split())
uf = UnionFind(n + 1)

for _ in range(m):
  cmd, a, b = map(int, input().split())
  if cmd:
    a = uf.find(a)
    b = uf.find(b)
    print('YES' if a == b else 'NO')
  else:
    uf.union(a, b)