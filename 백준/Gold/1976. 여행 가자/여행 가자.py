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

  def same_set(self, a, b):
    return self.find(a) == self.find(b)
  
n = int(input())
m = int(input())
uf = UnionFind(n + 1)

for i in range(n):
  for j, x in enumerate(list(map(int, input().split()))):
    if x:
      uf.union(i, j)

a = list(map(int, input().split()))
print('YES' if all(uf.same_set(a[i]-1, a[i+1]-1) for i in range(m-1)) else 'NO')