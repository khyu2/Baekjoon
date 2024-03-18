import sys
input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
  def __init__(self):
    self.p = [-1] * 200500

  def find(self, n):
    if self.p[n] < 0: return n
    self.p[n] = self.find(self.p[n])
    return self.p[n]

  def union(self, a, b):
    a = self.find(a)
    b = self.find(b)
    if a == b: return -self.p[a]
    self.p[a] += self.p[b]
    self.p[b] = a
    count = 1
    if self.p[a] < 0:
      count = max(count, -self.p[a])
    if self.p[b] < 0:
      count = max(count, -self.p[b])
    return count
  
  def __str__(self):
    return ' '.join(map(str, self.p[:10]))
  
for _ in range(int(input())):
  n = int(input())
  uf = UnionFind()
  a = {}

  idx = 0
  for i in range(n):
    x, y = input().split()
    if x not in a:
      a[x] = idx
      idx += 1
    if y not in a: 
      a[y] = idx
      idx += 1
    print(uf.union(a[x], a[y]))